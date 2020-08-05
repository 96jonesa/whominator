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


with nostdout():
    from whominator.whominator import correct_who_to_whom


def main():

    try:
        text = sys.argv[1]
        correct_who_to_whom(text)
    except:
        print("You must pass the text you want corrected as a command-line argument")
