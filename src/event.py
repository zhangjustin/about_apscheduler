import os
import logging
from datetime import datetime
from apscheduler.events import *

from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()

log = logging.getLogger('apscheduler.executors.default')
log.setLevel(logging.INFO)  # DEBUG

fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
h = logging.StreamHandler()
h.setFormatter(fmt)
log.addHandler(h)


LISTENER_JOB = (EVENT_JOB_ADDED |
                EVENT_JOB_REMOVED |
                EVENT_JOB_MODIFIED |
                EVENT_JOB_EXECUTED |
                EVENT_JOB_ERROR |
                EVENT_JOB_MISSED)


def job1():
    print ('job1', datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def job2():
    print ('job2', datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def job3(events):
    print 'evet happend'
    if events.code == EVENT_JOB_EXECUTED:
        print "Job %s has executed." % str(events.job_id)
    scheduler.shutdown()


a = scheduler.add_job(job2, 'interval',  seconds=3, id='aaa', name = '1')
b = scheduler.add_job(job1, 'interval',  seconds=5, id='bbb', name ='2')
scheduler.add_listener(job3, LISTENER_JOB)
scheduler.start()


