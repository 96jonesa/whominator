import setuptools

with open("requirements.txt") as f:
    required = f.read().splitlines()

setuptools.setup(
    name='whominator',
    version='0.1.0',
    description='corrects who to whom',
    url='https://github.com/96jonesa/whominator',
    author='96jonesa',
    author_email='ajones96@uw.edu',
    license='GNU General Public License v3 (GPLv3)',
    packages=setuptools.find_packages(),
    entry_points= {
        'console_scripts': ['whominate=whominator.whominate:main'],
    },
    python_requires='>=3.6',
    install_requires=required,
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
    ],
)
