from celery import task
from time import sleep
from celery.task.schedules import crontab  
from celery.decorators import periodic_task

@periodic_task(run_every=crontab(hour="0", minute="1", day_of_week="*"))
def hello():
    print "Nama saya bram"

@task
def start_vm(name,memory,template,vnc_port):
    pass
