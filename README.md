imgmanip
========
[![PyPI](https://img.shields.io/pypi/pyversions/satella.svg)](https://pypi.python.org/pypi/imgmanip)
[![PyPI version](https://badge.fury.io/py/satella.svg)](https://badge.fury.io/py/imgmanip)
[![PyPI](https://img.shields.io/pypi/implementation/satella.svg)](https://pypi.python.org/pypi/imgmanip)

Imgmanip is a library to write short scripts to process your images.

# How to use

You just issue a command
```imgmanip name_of_script file1 file2 ...```

Files will be modified in-place with provided script.
Script will be called on each file in sequence.
See [tests/script.py] to view a sample script that sets each 
non-alpha pixel to be black
