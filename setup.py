#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

from setuptools import setup
from setuptools.command.test import test as TestCommand

__version__ = '0.1.0'


def _requirements():
    if os.path.exists('requirements.txt'):
        with open('', 'r') as fd:
            return [name.strip() for name in fd.readlines()]


def _requirements_test():
    if os.path.exists('test_requirements.txt'):
        with open('test_requirements.txt', 'r') as fd:
            return [name.strip() for name in fd.readlines()]


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name="bingo",
    version=__version__,
    author="sgykfjsm",
    author_email="shigeyuki.fujishima@gmail.com",
    maintainer="sgykfjsm",
    maintainer_email="shigeyuki.fujishima@gmail.com",
    url="https://github.com/sgykfjsm/bingo",
    description="tiny bingo",
    long_description="tiny bingo",
    keywords="bingo",
    license='Apache License 2.0',
    packages=["bingo"],
    install_requires=_requirements(),
    tests_require=_requirements_test(),
    cmdclass={'test': PyTest},
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Topic :: Games/Entertainment :: Board Games"
    ]
)
