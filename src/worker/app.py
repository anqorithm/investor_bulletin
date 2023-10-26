""" Celery Application Creation """
"""_summary_
This script sets up a Celery application with a task schedule. 
It creates a Celery worker that will run the `check_thresholds` task every 5 minutes.
"""




from celery import Celery
from datetime import timedelta
def create_celery_app():
    app = Celery(
        'tasks',
        broker='pyamqp://guest:guest@localhost//',
        backend='rpc://',
        include=['tasks']
    )
    app.conf.beat_schedule = {
        'check_thresholds_every_5_minutes': {
            'task': 'tasks.check_thresholds',
            'schedule': timedelta(minutes=1),
        },
    }
    return app


celery_app = create_celery_app()
