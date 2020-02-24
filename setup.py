#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from setuptools import setup, find_packages
import richelieu

setup(
    name='richelieu',
    version=richelieu.__version__,
    packages=find_packages(),
    author=richelieu.__author__,
    author_email="fcoolranger@gmail.com",
    description="Random data generator that respect cardinality and data types",
    long_description=open('README.md').read(),
    include_package_data=True,
    url='http://github.com/NicoGGG/richelieu',
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 1 - Planning",
        "License :: OSI Approved",
        "Natural Language :: French",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Topic :: Data Generation",
    ],
    entry_points = {
        'console_scripts': [
            'richelieu = richelieu.__main__:main',
        ],
    },
    license="WTFPL",
)