# whominator

<a href="https://imgflip.com/i/4ahyja"><img src="https://i.imgflip.com/4ahyja.jpg" title="made at imgflip.com"/></a><div>

A tool for correcting 'who' to 'whom'.

Modified from the processing code for a Reddit bot described at https://github.com/96jonesa/rgb.

As described in the rgb repo, there are several hard-coded exceptions which are checked against to protect the tool from the bizzare grammatical situations that arise on internet forums. The tool prioritizes avoiding incorrect corrections.

It works by running the text through a dependency parser to check if 'who' is used as the object of a verb, then running through a named entity recognizer to determine if the 'who' is part of a proper noun, then checking against hard-coded exceptions.

# Installation

    pip install whominator
    python -m spacy download en_core_web_sm
    
Linux and macOS users: you may need to use sudo and/or pip3 and python3. You will know this is the case if it doesn't work without them.

Windows users: you may need to use --user and/or pip3 and python3. You will know this is the case if it doesn't work without them.

The spaCy en_core_web_sm model is 432 MB so it may take a while to download.

The flair named entity recognizer will download the first time you use either the command-line script or the imported function in Python.
    
# Command-Line Script

To use the command-line script to whominate some text, type the following in command-line:

    whominate "some text"
    
If you wish to use " characters inside the text, use the \ delimiter:

    whominate "do you know who he \"is\" throwing the 'ball' to?"
    
The corrected text is printed with asterisks surrounding the corrections.

# Import in Python

In Python you can import with:

    from whominator import whominator
    
The, whominator.whominate can take a single string as input and return the corrected text, without asterisks surrounding the corrections:

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
