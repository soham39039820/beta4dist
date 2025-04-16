# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 00:52:02 2025

@author: soham
"""

from setuptools import setup, find_packages

setup(
    name='beta4dist',  # Name of your package
    version='0.1.0',  # Version of your package
    packages=find_packages(),  # Automatically discover all packages
    description='A Python package for the Four-Parameter Beta Distribution and Likelihood-Based Estimation',
    long_description=open('README.md').read(),  # Read the README file for long description
    long_description_content_type='text/markdown',
    author='Soham Ghosh',
    author_email='phd2001161004@iiti.ac.in',
    url='https://github.com/soham39039820/beta4dist',
    license='MIT',  # Choose an appropriate license for your project
    classifiers=[  # Optional, but good practice
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[  # List any dependencies here
        'numpy',
        'scipy', # Add any other dependencies you need
    ],
    test_suite='tests',  # Specify the test directory
    tests_require=[  # Specify any additional testing dependencies
        'pytest',
    ],
)
