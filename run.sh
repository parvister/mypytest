#!/bin/bash

# Run only complex tests in arithmetic.test module. Example to pass the exact module name you want to test
python -m unittest -v packy.arithmetic.test.test_complex

# Run all tests in this package. Example of using discover
python -m unittest discover -v

# Running tests from within the package directory. Example of setting discover root path
cd packy/arithmetic
python -m unittest discover -v -t ../..
