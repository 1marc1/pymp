#!/usr/bin/env python3

# Python Multiprocessing (pymp) is an example of how to implement:
# * Python Multiprocessing that returns results.
# * Performs logging from all functions to a main log file.
# * Can be frozen and still works in a Windows environment.

# This file contains common functions.

import os
import tempfile
import logging
import multiprocessing
import pymp_global as gv

def MP_Init_Log():
    _logfile = os.path.join(tempfile.gettempdir(),gv.GeneralLogFileName)
    gv.logger = logging.getLogger('pymp')
    file_handler = logging.handlers.RotatingFileHandler(_logfile, maxBytes=gv.GeneralLogSize, backupCount=gv.GeneralLogCount)
    file_handler.setFormatter(logging.Formatter(gv.GeneralLogFormat))
    gv.logger.addHandler(file_handler)

def MPFunction():
    gv.logger.info('Starting Multiprocessing function')
    AuxFunction('MPFunction')

    MyList = ['a','b','c']
    pool = multiprocessing.Pool(initializer=MP_Init_Log)
    result = pool.map(MPWorker, MyList)
    pool.terminate()

    print ('Results: ' + str(result))

def MPWorker(MyListItem):
    gv.logger.info('MP Processing ' + MyListItem)
    ReturnValue = AuxFunction(MyListItem)
    return [ReturnValue, ReturnValue]

def AuxFunction(MyValue):
    gv.logger.info('Starting AuxFunction for ' + str(MyValue))
    return MyValue + '1'
