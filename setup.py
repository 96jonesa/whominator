import setuptools

setuptools.setup(
    name='whominator',
    version='0.1.0',
    description='corrects who to whom',
    url='https://github.com/96jonesa/whominator',
    author='96jonesa',
    author_email='ajones96@uw.edu',
    license='GPLv3',
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=['torch>=1.1.0',
                      'spacy',
                      'flair',
                      ],

    classifiers=[
        'License :: OSI Approved :: GPLv3 License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
    ],
)
