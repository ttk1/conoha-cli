#!/usr/bin/env python

from setuptools import setup, find_packages

entry_points = {
    'console_scripts': [
        'conoha = conoha.__main__:main'
    ]
}

setup(
    name='conoha',
    version='1.0.0',
    description='ConoHa API Client',
    author='tama@ttk1',
    author_email='tama@ttk1.net',
    url='https://github.com/ttk1/conoha-cli',
    packages=find_packages(exclude=('test',)),
    entry_points=entry_points
)