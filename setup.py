#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_requires():
    requires = []

    with open('requirements.txt') as file:
        for line in file:
            requires.append(line.strip())

    return requires


setup(
    name='post-shift-client',
    version='1.0.0',
    description='Simple client for the post-shift.ru',
    author='Sergey Demenok',
    author_email='sergey.demenok@gmail.com',
    url='https://github.com/efpato/post-shift-client',
    py_modules=['post_shift_client'],
    install_requires=get_requires()
)
