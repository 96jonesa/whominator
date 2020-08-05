# whominator

<a href="https://imgflip.com/i/4ahyja"><img src="https://i.imgflip.com/4ahyja.jpg" title="made at imgflip.com"/></a><div>

A tool for correcting 'who' to whom'.

Modified from the processing code for a Reddit bot described at https://github.com/96jonesa/rgb.

As described in the rgb repo, there are several hard-coded exceptions which are checked against to protect the tool from the bizzare grammatical situations that arise on internet forums. The tool prioritizes avoiding incorrect corrections.

It works by running the text through a dependency parser to check if 'who' is used as the object of a verb, then running through a named entity recognizer to determine if the 'who' is part of a proper noun, then checking against hard-coded exceptions.

# Installation

    pip install whominator
    python -m spacy download en_core_web_sm
    
# Command-Line Script

To use the command-line script to whominate some text, type the following in command-line:

    whominate "some text"
    
Or, if you prefer single-quotes:

    whominate 'some text'
    
If you wish to use ' or " characters inside the text, use the \ delimiter:

    whominate "do you know who he \"is\" throwing the 'ball' to?"
    
Or

    whominate 'do you know who he \'is\' throwing the "ball" to?"
    
Only use the \ delimiter for the same type of quotes you are surrounding the text with (do not delimit ' in text surrounded by ", or vice versa, or the \ will be considered part of the text).

# Import in Python

In python you can use

    import whominator.whominate
    
which takes a single string as input and prints the corrected text.

# Soon to Come

I will update exceptions to include those currently in use on the bot.

I will modify whominator.whominate to return the corrected string, without asterisks surrounding the corrections, instead of printing it.

I will add the spaCy model download to the pip install to make installation simpler.
