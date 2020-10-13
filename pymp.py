#!/usr/bin/env python3

# Python Multiprocessing (pymp) is an example of how to implement:
# * Python Multiprocessing that returns results.
# * Performs logging from all functions to a main log file.
# * Can be frozen and still works in a Windows environment.

# This file contains the main code.

import os
import logging
import logging.handlers
import tempfile
import multiprocessing
import pymp_global as gv

def init_log():
    _logfile = os.path.join(tempfile.gettempdir(),gv.GeneralLogFileName)
    gv.logger = logging.getLogger('pymp')
    gv.logger.setLevel(logging.DEBUG)
    file_handler = logging.handlers.RotatingFileHandler(_logfile, maxBytes=gv.GeneralLogSize, backupCount=gv.GeneralLogCount)
    file_handler.setFormatter(logging.Formatter(gv.GeneralLogFormat))
    gv.logger.addHandler(file_handler)

def MyFunction():
    gv.logger.info('Info log from MyFunction')

if __name__ == "__main__":
    multiprocessing.freeze_support()
    gv.GeneralLogFileName = 'pymp.log'
    init_log()
    gv.logger.info('Starting pymp')
    MyFunction()
