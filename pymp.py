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

def listener_configurer():
    root = logging.getLogger()
    #h = logging.handlers.RotatingFileHandler('mptest.log', 'a', 300, 10)
    h = logging.handlers.RotatingFileHandler(gv.GeneralLogFileName, maxBytes=gv.GeneralLogSize, backupCount=gv.GeneralLogCount)
    #f = logging.Formatter('%(asctime)s %(processName)-10s %(name)s %(levelname)-8s %(message)s')
    f = logging.Formatter(gv.GeneralLogFormat)
    h.setFormatter(f)
    root.addHandler(h)

def listener_process(queue, configurer):
    configurer()
    while True:
        try:
            record = queue.get()
            if record is None:  # We send this as a sentinel to tell the listener to quit.
                break
            logger = logging.getLogger(record.name)
            logger.handle(record)  # No level or filter logic applied - just do it!
        except Exception:
            import sys, traceback
            print('Whoops! Problem:', file=sys.stderr)
            traceback.print_exc(file=sys.stderr)

def worker_configurer(queue):
    h = logging.handlers.QueueHandler(queue)  # Just the one handler needed
    root = logging.getLogger()
    root.addHandler(h)
    # send all messages, for demo; no other level or filter logic applied.
    root.setLevel(logging.DEBUG)

def main():
    queue = multiprocessing.Queue(-1)
    listener = multiprocessing.Process(target=listener_process,
                                       args=(queue, listener_configurer))
    listener.start()

    #logger = logging.getLogger('test')
    #logger.info('Starting pymp')
    MyFunction(queue, worker_configurer)

    queue.put_nowait(None)
    listener.join()


def MyFunction(queue, configurer):
    configurer(queue)
    logger = logging.getLogger('test')
    logger.info('Starting MyFunction')
    #dc.MPFunction()

if __name__ == "__main__":
    multiprocessing.freeze_support()
    gv.GeneralLogFileName = 'pymp.log'
    main()



