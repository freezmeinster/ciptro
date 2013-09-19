from __future__ import absolute_import
from celery import Celery

#### Settings ##########
celery_object = 'metranet_celery.celery'
celery_broker = 'amqp://10.10.2.59'
celery_backend = "amqp://10.10.2.59"
celery_include=['metranet_celery.tasks']

celery = Celery( celery_object,
broker=celery_broker,
backend=celery_backend,
include=celery_include)

celery.conf.update(
CELERY_TASK_RESULT_EXPIRES = 3600,
CELERYD_CONCURRENCY=1
)

if __name__ == "__main__" :
    celery.start()