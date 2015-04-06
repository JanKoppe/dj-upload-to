#!/usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from setuptools import setup
import os
import dj_upload_to


ROOT_PACKAGE = 'dj-upload-to'
VERSION = dj_upload_to.__version__
DESCRIPTION = 'Small application that simplifies naming of uploaded files'
DIR = os.path.dirname(__file__)


def long_description():
    """
    Returns package long description from README
    """
    def read(what):
        with open(os.path.join(DIR, '%s.rst' % what)) as fp:
            return fp.read()
    return '{README}\n'.format(README=read('README'))


if __name__ == '__main__':
    setup(name=ROOT_PACKAGE,
          description=DESCRIPTION,
          author='Mikhail Porokhovnichenko',
          author_email='marazmiki@gmail.com',
          url='https://github.com/marazmiki/django-webdav-storage',
          version=VERSION,
          long_description=long_description(),
          py_modules=['dj_upload_to'],
          test_suite='tests.main',
          zip_safe=False,
          classifiers=[
              'Environment :: Web Environment',
              'Programming Language :: Python :: 2.7',
              'Programming Language :: Python :: 3.3',
              'Programming Language :: Python :: 3.4',
              'Framework :: Django'
          ])