# whominator

<a href="https://imgflip.com/i/4ahyja"><img src="https://i.imgflip.com/4ahyja.jpg" title="made at imgflip.com"/></a><div>

A tool for correcting 'who' to 'whom'.

Modified from the processing code for a Reddit bot described at https://github.com/96jonesa/rgb.

As described in the rgb repo, there are several hard-coded exceptions which are checked against to protect the tool from the bizzare grammatical situations that arise on internet forums. The tool prioritizes avoiding incorrect corrections.

It works by running the text through a dependency parser to check if 'who' is used as the object of a verb, then running through a named entity recognizer to determine if the 'who' is part of a proper noun, then checking against hard-coded exceptions.

# Requirements

Python 3.6 or newer.

# Installation

    pip install whominator
    python -m spacy download en_core_web_sm
    
Linux and macOS users: you may need to use sudo and/or pip3 and python3. You will know this is the case if it doesn't work without them.

Windows users: you may need to use --user and/or pip3 and python3. You will know this is the case if it doesn't work without them.

The spaCy en_core_web_sm model is 432 MB so it may take a while to download.

The models will be cached the first time you use either the command-line script or the imported function in Python - this takes some time.

If you are using Windows and experience an error in the (automated) installation of PyTorch (which is a dependency for flair), try the tip from https://docs.python.org/3.7/using/windows.html section 3.1.2. If that does not work, then you have run into a compatibility issue with the newest versions of Pytorch, Python, and Windows. If that is the case, then you must install an older version of Pytorch:

    pip install torch==1.2.0+cpu torchvision==0.4.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
    
# Command-Line Script

To use the command-line script to whominate some text, type the following in command-line:

    whominate "some text"
    
If you wish to use " characters inside the text, use the \ delimiter:

    whominate "do you know who he \"is\" speaking to, or 'don't' you?"
    
The corrected text is printed with asterisks surrounding the corrections.

# Import in Python

In Python you can import with:

    from whominator import whominator
    
The function whominator.whominate takes a single string as input and returns the corrected text, without asterisks surrounding the corrections:

    whominator.whominate("""some text""")
    
To avoid using delimeters in hard-coded strings, I advise surrounding the text in triple-qoutes ("""some text""") as opposed to single-qoutes ('some text') or double-quotes ("some text"). If you do this, you will only have to delimit double-quotes at the very end of the text (to avoid ending with more than three quotes).

# Soon to Come

I will add the spaCy model download to the pip install to make installation simpler.

# Citations

    @inproceedings{akbik2018coling,
      title={Contextual String Embeddings for Sequence Labeling},
      author={Akbik, Alan and Blythe, Duncan and Vollgraf, Roland},
      booktitle = {{COLING} 2018, 27th International Conference on Computational Linguistics},
      pages     = {1638--1649},
      year      = {2018}
    }
