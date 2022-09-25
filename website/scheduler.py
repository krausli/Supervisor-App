from pytz import utc

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ProcessPoolExecutor


jobstores = {
    'mongo': {'type': 'mongodb'},
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}
executors = {
    'default': {'type': 'threadpool', 'max_workers': 20},
    'processpool': ProcessPoolExecutor(max_workers=5)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 3
}
scheduler = BackgroundScheduler()

#change this when can
def job_function():
    print('Hello World')

#automated reminder email
scheduler.add_job(job_function, 'cron', day_of_week='mon-fri', hour=9, minute=13, end_date='2020-06-05 09:14:00')  


# maybe add jobs

scheduler.configure(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)

scheduler.start()