from django.shortcuts import render_to_response
from django.template import RequestContext
from cicip.models import Version

def home(request):
    version = Version.objects.filter(aktif=True)
    return render_to_response("index.html",{
        'list_distro' : version
    },context_instance=RequestContext(request))

def nyicip(request):
    return render_to_response("nyicip.html",{
    },context_instance=RequestContext(request))

def kenal(request):
    return render_to_response("kenal.html",{
    },context_instance=RequestContext(request))