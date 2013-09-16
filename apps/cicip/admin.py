from django.contrib import admin
from cicip.models import  Distro, Version, TemplateOS, Pesan, ProfilPengguna

admin.site.register(Pesan)
admin.site.register(Distro)
admin.site.register(Version)
admin.site.register(TemplateOS)
admin.site.register(ProfilPengguna)