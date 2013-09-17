from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from cicip.models import Version
from virt.models import VirtualMachine
from django.contrib import messages

def home(request):
    version = Version.objects.filter(aktif=True)
    return render_to_response("index.html",{
        'list_distro' : version
    },context_instance=RequestContext(request))

def nyicip(request):
    vm = VirtualMachine.objects.filter(user=request.user)
    return render_to_response("nyicip.html",{
        'vm_list' : vm
    },context_instance=RequestContext(request))

def kenal(request):
    return render_to_response("kenal.html",{
    },context_instance=RequestContext(request))

def tambah_cicip(request,version_id):
    version = Version.objects.get(id=version_id)
    virt = VirtualMachine.objects.filter(user=request.user,distro_version=version)
    if len(virt) > 0 :
        messages.add_message(request, messages.WARNING, 'Maaf anda sudah meminta disto ini untuk di cicipi')
        return redirect('nyicip')
    else :
        vm = VirtualMachine(
            vnc_port = 0,
            websocket_port = 0,
            user = request.user,
            distro_version = version,
            mem = version.templateos.min_memory,
            state = 'down'
        )
        vm.save()
        
        messages.add_message(request, messages.SUCCESS, 'Permintaan coba distro %s %s telah ditambahkan. Sistem akan menjadwalkan distro anda untuk menyala, silangkah tunggu.' \
        %(vm.distro_version.distro, vm.distro_version.version))
        return redirect('nyicip')

def nonton_cicip(request,id):
    return render_to_response("nonton.html",{
    },context_instance=RequestContext(request))