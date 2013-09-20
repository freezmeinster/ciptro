from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from cicip.models import Version
from virt.models import VirtualMachine
from django.contrib import messages
from port_generator import get_vnc_port, get_ws_port
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    version = Version.objects.filter(aktif=True)
    return render_to_response("index.html",{
        'list_distro' : version
    },context_instance=RequestContext(request))

@login_required
def nyicip(request):
    vm = VirtualMachine.objects.filter(user=request.user, active=True)
    return render_to_response("nyicip.html",{
        'vm_list' : vm
    },context_instance=RequestContext(request))

@login_required
def kenal(request):
    return render_to_response("kenal.html",{
    },context_instance=RequestContext(request))

@login_required
def tambah_cicip(request,version_id):
    version = Version.objects.get(id=version_id)
    virt = VirtualMachine.objects.filter(user=request.user,distro_version=version,active=True)
    if len(virt) > 0 :
        messages.add_message(request, messages.WARNING, 'Maaf anda sudah meminta disto ini untuk di cicipi')
        return redirect('nyicip')
    else :
        vm = VirtualMachine(
            vnc_port = get_vnc_port(),
            websocket_port = get_ws_port(),
            user = request.user,
            distro_version = version,
            mem = version.templateos.min_memory,
            state = 'down'
        )
        vm.save()
        
        messages.add_message(request, messages.SUCCESS, 'Permintaan coba distro %s %s telah ditambahkan. Sistem akan menjadwalkan distro anda untuk menyala, silangkah tunggu.' \
        %(vm.distro_version.distro, vm.distro_version.version))
        return redirect('nyicip')

@login_required
def nonton_cicip(request,id):
    vm = VirtualMachine.objects.get(id=id)
    return render_to_response("nonton.html",{
        'vm':vm
    },context_instance=RequestContext(request))

@login_required
def hapus_cicip(request,id):
    vm = VirtualMachine.objects.get(id=id)
    vm.active = False
    vm.save()
    messages.add_message(request, messages.SUCCESS, 'Permintaan coba distro %s %s telah dihapus dari sistem' \
        %(vm.distro_version.distro, vm.distro_version.version))
    return redirect('nyicip')

def login_page(request):
    return render_to_response("login.html",{
    },context_instance=RequestContext(request))

def logout_page(request):
    pass