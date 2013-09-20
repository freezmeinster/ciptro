from django.db import models
from cicip.models import Version
from django.contrib.auth.models import User
    

class VirtualMachine(models.Model):
    STATE = (
        ("up", "Running"),
        ("down", "Stop"),
    )
    vnc_port = models.CharField(max_length=5)
    websocket_port = models.CharField(max_length=5)
    reg_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    distro_version = models.ForeignKey(Version)
    mem = models.IntegerField()
    state = models.CharField(max_length=10,choices=STATE, default="up")
    active = models.BooleanField(default=True)
    
    def __unicode__(self):
        return "%s oleh %s" %(self.distro_version, self.user.get_full_name() )
    
