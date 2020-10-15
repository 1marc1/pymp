#!/usr/bin/env python3

# Python Multiprocessing (pymp) is an example of how to implement:
# * Python Multiprocessing that returns results.
# * Performs logging from all functions to a main log file.
# * Can be frozen and still works in a Windows environment.

# This file contains common functions.

import multiprocessing
import pymp_global as gv

from logging import getLogger

logger = getLogger('pycommon')

def MPFunction():
    logger.info('Starting Multiprocessing function')
    AuxFunction('MPFunction')

    MyList = ['a','b','c']
    pool = multiprocessing.Pool()
    result = pool.map(MPWorker, MyList)
    pool.terminate()

    print ('Results: ' + str(result))

def MPWorker(MyListItem):
    logger.info('MP Processing ' + MyListItem)
    ReturnValue = AuxFunction(MyListItem)
    return [ReturnValue, ReturnValue]

def AuxFunction(MyValue):
    logger = getLogger('aux')
    logger.info('Starting AuxFunction for ' + str(MyValue))
    return MyValue + '1'
