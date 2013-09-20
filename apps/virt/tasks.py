import os
from celery import task
from time import sleep
from celery.task.schedules import crontab  
from celery.decorators import periodic_task
from virt.models import VirtualMachine
from subprocess import Popen
from django.conf import settings


def start_vm(memory,template,vnc_port):
    if template.jenis == "livecd" :
        src = "-cdrom"
    elif template.jenis == "disk" :
        src = "-hda"
        
    app = "/usr/bin/qemu-kvm"
    args = " -m %s %s %s -enable-kvm -vnc localhost:%s -usbdevice tablet" % (memory, src, template.file_path, vnc_port)
    Popen(app + args, shell=True)

def start_vnc_proxy(vnc_port,ws_port):
    port = int(vnc_port) + 5900
    app = os.path.join(settings.ROOT_PATH,'libs/novnc/websockify')
    arg = " %s 127.0.0.1:%s" % (ws_port,str(port))
    Popen(app + arg, shell=True)
    

@periodic_task(run_every=crontab(minute="*/1"))
def scan_vm_request():
    vm_up = VirtualMachine.objects.filter(state='down',active=True)
    for vm in vm_up:
        vm.state = "up"
        vm.save()
        start_vm(vm.mem,vm.distro_version.templateos,vm.vnc_port)
        print "Menyalakan %s, milik %s" % (vm.distro_version, vm.user.get_full_name())
        start_vnc_proxy(vm.vnc_port,vm.websocket_port)
        print "Menyalakan Websocket proxy pada port %s untuk vnc port %s" %(vm.vnc_port,vm.websocket_port)
    return "Done"
    
