from django.contrib import admin
from cicip.models import  Distro, Version, TemplateOS

admin.site.register(Distro);
admin.site.register(Version);
admin.site.register(TemplateOS);