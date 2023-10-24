#!/usr/bin/env python
from setuptools import find_packages, setup

with open("README.md", "r") as des:
    l_desc = des.read()

setup(
    name='pymozhitranslate',
    packages=find_packages(),
    version='0.1.3',
    entry_points={'console_scripts': ['mozhitranslate = pymozhitranslate.cli:translate']},
    description='Simple translator using mozhi API translate',
    license='MIT',
    long_description=l_desc,
    long_description_content_type='text/markdown',
)
