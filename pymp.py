#!/usr/bin/env python3

# Python Multiprocessing (pymp) is an example of how to implement:
# * Python Multiprocessing that returns results.
# * Performs logging from all functions to a main log file.
# * Can be frozen and still works in a Windows environment.

# This file contains the main code.

'''
After running, the output on the screen should be:
Results: [['a1', 'a1'], ['b1', 'b1'], ['c1', 'c1']]

And the output in the pymp.log file (in the temporary directory) should be similar to:
2020-10-13 23:25:06,732 pymp     INFO     MainProcess Starting pymp
2020-10-13 23:25:06,732 pymp     INFO     MainProcess Starting MyFunction
2020-10-13 23:25:06,732 pymp     INFO     MainProcess Starting Multiprocessing function
2020-10-13 23:25:06,732 pymp     INFO     MainProcess Starting AuxFunction for MPFunction
2020-10-13 23:25:06,746 pymp     INFO     ForkPoolWorker-2 MP Processing b
2020-10-13 23:25:06,746 pymp     INFO     ForkPoolWorker-3 MP Processing c
2020-10-13 23:25:06,747 pymp     INFO     ForkPoolWorker-2 Starting AuxFunction for b
2020-10-13 23:25:06,747 pymp     INFO     ForkPoolWorker-3 Starting AuxFunction for c
2020-10-13 23:25:06,746 pymp     INFO     ForkPoolWorker-1 MP Processing a
2020-10-13 23:25:06,747 pymp     INFO     ForkPoolWorker-1 Starting AuxFunction for a
'''

import os
import tempfile
import logging
import logging.handlers
import multiprocessing
import pymp_global as gv
import pymp_common as dc

def init_log():
    _logfile = os.path.join(tempfile.gettempdir(),gv.GeneralLogFileName)
    gv.logger = logging.getLogger('pymp')
    gv.logger.setLevel(logging.DEBUG)
    file_handler = logging.handlers.RotatingFileHandler(_logfile, maxBytes=gv.GeneralLogSize, backupCount=gv.GeneralLogCount)
    file_handler.setFormatter(logging.Formatter(gv.GeneralLogFormat))
    gv.logger.addHandler(file_handler)

def MyFunction():
    gv.logger.info('Starting MyFunction')
    dc.MPFunction()

if __name__ == "__main__":
    multiprocessing.freeze_support()
    gv.GeneralLogFileName = 'pymp.log'
    init_log()
    gv.logger.info('Starting pymp')
    MyFunction()
