from random import randint
from virt.models import VirtualMachine

def get_vnc_port():
    vm_list = VirtualMachine.objects.all()
    port_list = []
    for vm in vm_list:
        port_list.append(vm.vnc_port)
    while True :
        port = randint(0,100)
        if port not in port_list :
            return port
            break
        
def get_ws_port():
    vm_list = VirtualMachine.objects.all()
    port_list = []
    for vm in vm_list:
        port_list.append(vm.websocket_port)
    
    while True :
        port = randint(6080,6180)
        if port not in port_list :
            return port
            break