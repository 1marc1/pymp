#!/usr/bin/env python3

# Python Multiprocessing (pymp) is an example of how to implement:
# * Python Multiprocessing that returns results.
# * Performs logging from all functions to a main log file.
# * Can be frozen and still works in a Windows environment.

# This file contains common functions.

def MPFunction():
    gv.logger.info('Starting Multiprocessing function')

def AuxFunction():
    gv.logger.info('Starting Auxiliary function')
