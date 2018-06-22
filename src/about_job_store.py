from pytz import utc
from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor


def tick():
    print('Tick! The time is: %s' % datetime.now())

def hello_world(text):
    print 'hell-{}'.format(text)

def get_job_list():
    print '----'
    scheduler.print_jobs()
    print '<----->'

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
scheduler = BlockingScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)
scheduler.add_job(tick, 'interval', seconds=5, name='time tick')
scheduler.add_job(get_job_list, 'interval', seconds=3, name='job list')
scheduler.add_job(hello_world, 'interval', seconds=3, args=['world'], name='test paremeter')
scheduler.start()

