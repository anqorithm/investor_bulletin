# app.py
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
