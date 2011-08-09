# -*- coding: utf-8 -*-
from distutils.core import setup

import dicts

setup(name = 'dicts',
      version = dicts.__version__,
      description = 'Easy use dictionaries with specific features',
      long_description = open('README.rst').read(),
      author = dicts.__author__,
      author_email = dicts.__email__,
      url = 'https://github.com/moliware/dicts',
      packages = ['dicts'],
      license = 'LGPL',
      classifiers = ('Development Status :: 5 - Production/Stable',
                     'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
                     'Natural Language :: English',
                     'Programming Language :: Python :: 2.5',
                     'Programming Language :: Python :: 2.6',
                     'Programming Language :: Python :: 2.7',
      ),
)
