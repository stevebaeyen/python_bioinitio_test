#!/usr/bin/env python

from distutils.core import setup

LONG_DESCRIPTION = \
'''The program reads one or more input FASTA files.
For each file it computes a variety of statistics, and then
prints a summary of the statistics as output.

The goal is to provide a solid foundation for new bioinformatics command line tools,
and is an ideal starting place for new projects.'''


setup(
    name='python_bioinitio_test',
    version='0.1.0.0',
    author='Steve Baeyen',
    author_email='steve.baeyen@ilvo.vlaanderen.be',
    packages=['python_bioinitio_test'],
    package_dir={'python_bioinitio_test': 'python_bioinitio_test'},
    entry_points={
        'console_scripts': ['python_bioinitio_test = python_bioinitio_test.python_bioinitio_test:main']
    },
    url='https://github.com/stevebaeyen/python_bioinitio_test',
    license='LICENSE',
    description=('A prototypical bioinformatics command line tool'),
    long_description=(LONG_DESCRIPTION),
    install_requires=["biopython"],
)
