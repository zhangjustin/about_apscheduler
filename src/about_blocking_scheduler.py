import os
from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler


def job1():
    print (datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def job2():
    with open('./test.log', 'a+') as f:
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(time_now)
        f.write('\n')

scheduler = BlockingScheduler()


@scheduler.scheduled_job('interval', seconds=5, id='aaa')
def job3():
    print 'this is a joke'


scheduler.add_job(job2, 'interval',  seconds = 3)
scheduler.add_job(job1, 'interval',  seconds = 3)
scheduler.start()
print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

