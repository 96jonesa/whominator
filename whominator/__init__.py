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
    from whominator import whominator

__author__ = '96jonesa'
__version__ = '0.1.1'
