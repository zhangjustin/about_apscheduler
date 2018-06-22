import os
import logging
from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()

log = logging.getLogger('apscheduler.executors.default')
log.setLevel(logging.INFO)  # DEBUG

fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
h = logging.StreamHandler()
h.setFormatter(fmt)
log.addHandler(h)


def job1():
    print ('job1', datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def job2():
    print ('job2', datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def job3():
    print 'modify job'
    scheduler.modify_job('bbb', name='modified name')
    scheduler.reschedule_job('bbb', trigger='interval',seconds=10)

a = scheduler.add_job(job2, 'interval',  seconds=3, id='aaa', name = '1')
b = scheduler.add_job(job1, 'interval',  seconds=3, id='bbb', name ='2')
scheduler.add_job(job3, 'interval', seconds=5, id='ccc')
scheduler.start()
print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
