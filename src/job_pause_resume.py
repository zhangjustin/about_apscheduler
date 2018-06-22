from pytz import utc
from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor


def tick():
    print('Tick! The time is: %s' % datetime.now())

def hello_world(text):
    print 'hell-{}'.format(text)

def stop_job(job_id):
    print 'will stop job {}'.format(job_id)
    scheduler.pause_job(job_id)

def start_job(job_id):
    print 'will start job {}'.format(job_id)
    scheduler.resume_job(job_id)

jobstores = {
    'default': SQLAlchemyJobStore(url='mysql+pymysql://juwai:password@192.168.222.9:3306/juwai?use_unicode=0')
}
executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(1)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 1
}
scheduler = BlockingScheduler( executors=executors, job_defaults=job_defaults, timezone=utc)
d = scheduler.add_job(tick, 'interval', seconds=5, name='time tick', id = 'aaa')
c= scheduler.add_job(hello_world, 'interval', seconds=3, args=['world'], name='test paremeter', id='bbb')
scheduler.add_job(stop_job, 'interval', seconds=10, args=[c], name='stop job')
scheduler.add_job(start_job, 'interval', seconds=20, args=['aaa'], name='start job')

scheduler.start()
