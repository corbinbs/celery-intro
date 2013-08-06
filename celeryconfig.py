from celery.schedules import crontab
from datetime import timedelta

BROKER_URL = 'sqla+sqlite:///celerydb.sqlite'

CELERY_RESULT_BACKEND = "database"
CELERY_RESULT_DBURI = "sqlite:///celerydb.sqlite"

#Always eager can be turned on (set to True) to run all tasks in-line
#This can be useful for debugging/testing
CELERY_ALWAYS_EAGER = False
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True

#Register celery tasks
CELERY_IMPORTS = (
    'tasks',
)

CELERY_ANNOTATIONS = {"tasks.add": {"rate_limit": "10/s"}}

CELERY_TIMEZONE = 'US/Eastern'

#http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html#entries
CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'tasks.add',
        'schedule': timedelta(seconds=30),
        'args': (16, 16)
    },
    #http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html#crontab-schedules
    'archive-old-data': {
        'task': 'tasks.archive_old_data',
        'schedule': crontab(day_of_month=1),
        'args': []
    },
}

CELERYBEAT_SCHEDULE_FILENAME = 'celery-schedule'
