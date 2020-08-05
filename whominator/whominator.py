import spacy
from flair.data import Sentence
from flair.models import SequenceTagger
from flair.tokenization import SegtokTokenizer
import time
import contextlib
import sys

# there is an annoying loading printout from flair's NER tagger.
# this suppression must also surround imports to avoid the printout.
class DummyFile(object):
    def write(self, x): pass

@contextlib.contextmanager
def nostdout():
    save_stdout = sys.stdout
    sys.stdout = DummyFile()
    yield
    sys.stdout = save_stdout


nlp = spacy.load('en_core_web_sm')

with nostdout():
    tagger = SequenceTagger.load('ner')

# checks for various surrounding tokens which produce false flags
# due to the typically terrible overall grammar and prevelance of
# typos in forum posts written with these.
def check_for_exceptions(doc, token):

    i = token.i

    if i > 0 and doc[i - 1].text.lower() in ['the', '\"']:
        return True

    if len(doc) > i + 1:
        if doc[i + 1].text.lower in ['tf', '\"']:
            return True
        if doc[i + 1].text[0] == '\'':
            return True

    if len(doc) > i + 2:
        the_check = doc[i + 1].text.lower() in ['the', 'teh', 'th3', 't3h', 'da', 'd4', 'tha', 'th4', 't']
        fuck_check = doc[i + 2].text.lower() in ['fuck', 'fck', 'fk', 'f', 'fuuck', 'fuuuck', 'fuuuuck', 'fuuuuuck']

        if the_check and fuck_check:
            return True

    return False


# use all caps or Spongebob-case if being used, otherwise append lowercase m.
# surrounds with * on each side to emphasize the corrected word - on reddit
# this italicizes the word.
def whom_string(who_string_with_ws):

    result = ''

    who_string = who_string_with_ws[:3]

    if who_string == 'WHO':
        result = '*WHOM*'
    elif who_string == 'wHo':
        result = '*wHoM*'
    else:
        result = '*' + who_string + 'm*'

    if len(who_string_with_ws) > 3:
        return result + ' '
    else:
        return result


# checks if 'who' is used where 'whom' should be used (i.e. as an object), and
# for each such instance prints the text along with a correction to 'whom'
# either starting at 'whom' and ending with the relevant verb/root, or vice versa.
def correct_who_to_whom(text):

    doc = nlp(text)

    tokenized_text = []

    phrases = []

    token_number = 0

    for token in doc:

        tokenized_text.append(token.text_with_ws)

        token_number += 1

        # it is very difficult for named entity recognizer to recognize 'Who'
        # in isolation - the motivating text was repeated exclamation of
        # 'Who! Who!' in a The Grinch fan fiction.
        if token.text.lower() in ['grinch', 'whoville']:
            return

        if token.text.lower() == 'who' :
            if token.dep_ in ['dobj', 'iobj', 'pobj']:

                # check for the hard-coded exceptions
                if not check_for_exceptions(doc, token):
                    should_be_whom = True

                    sentence = Sentence(text, use_tokenizer=SegtokTokenizer())
                    tagger.predict(sentence)

                    # make sure it is not part of a named entity
                    for entity in sentence.get_spans('ner'):
                        if token.idx >= entity.start_pos and token.idx <= entity.end_pos:
                            should_be_whom = False

                    if should_be_whom:

                        # detokenizes the corrected excerpt (e.g. removes added space
                        # between last word in sentence and punctutation, rejoins
                        # don and 't to form don't, etc., only if such joins were
                        # present in the original text)
                        tokenized_text[token.i] = whom_string(token.text_with_ws)

    # prints the text with corrections made (corrections surround by asterisks)
    corrected_text = ''.join([tkn for tkn in tokenized_text])
    print(corrected_text)


def whominate(text):
    correct_who_to_whom(text)
