#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages
import os
import codecs

setup_path = os.path.abspath(os.path.dirname(__file__))

setup(name='manim',
      version='0.1',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
      ],
      python_requires='>=3',      

      packages=find_packages())

