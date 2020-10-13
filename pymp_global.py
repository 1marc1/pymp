#!/usr/bin/env python3

# Python Multiprocessing (pymp) is an example of how to implement:
# * Python Multiprocessing that returns results.
# * Performs logging from all functions to a main log file.
# * Can be frozen and still works in a Windows environment.

# This file contains global variables.

logger = None
GeneralLogFileName = ''
GeneralLogFormat = '%(asctime)s %(name)-8s %(levelname)-8s %(processName)-10s %(message)s'
GeneralLogSize = 100000
GeneralLogCount = 4
