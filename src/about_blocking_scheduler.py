from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

from datetime import datetime
import time
import os

def job1():
    print (datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def job2():
    with open('./test.log', 'a+') as f:
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(time_now)
        f.write('\n')
        # f.close()

# scheduler = BlockingScheduler()

scheduler = BackgroundScheduler()

scheduler.add_job(job2, 'interval',  seconds = 3)
scheduler.start()
print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

try:
    # This is here to simulate application activity (which keeps the main thread alive).
    while True:
        time.sleep(2)
except (KeyboardInterrupt, SystemExit):
    # Not strictly necessary if daemonic mode is enabled but should be done if possible
    scheduler.shutdown()
