#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from os import path
from io import open

with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'),
          encoding='utf-8') as f:
    long_description = f.read()

setup(
    # Basic project information
    name='python3-boilerplate',
    version='0.0.1',
    # Authorship and online reference
    author='Basti Tee',
    author_email='basti.tee@posteo.de',
    url='https://github.com/BastiTee/python3-boilerplate',
    # Detailled description
    description='Python3 boilerplate module.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='sample setuptools development',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    # Package configuration
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=[],
    # Licensing and copyright
    license='Apache 2.0',
    copyright='Copyright 2019 basti.tee',
)
