__author__ = 'ruslanpa'

from os.path import join, dirname

from setuptools import setup, find_packages

import app, test


setup(name='currency_cash',
      author='ruslanpa',
      author_email='ruslan.pavlutskiy@gmail.com',
      version=app.__version__,
      packages=find_packages(),
      long_description=open(join(dirname(__file__), 'README.md')).read(),
      requires=['flask', 'requests'],
      test_suite=app.tests.__name__
)
