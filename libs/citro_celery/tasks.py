from __future__ import absolute_import

import os
import commands
from metranet_celery.celery import celery


@celery.task
def pull_oe_module():
    os.chdir(OE_APP_DIR)
    commands.getoutput("sudo git pull origin master")
    return "oe-pulled"