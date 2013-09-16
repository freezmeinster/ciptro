from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.template.defaultfilters import safe
from django.conf import settings

class ProfilPengguna(models.Model):
    KELAMIN = (
        ("L","Laki-laki"),
        ("P","Perempuan"),
    )
    
    user = models.OneToOneField(User)
    jenis_kelamin = models.CharField(max_length=10, choices=KELAMIN)
    
    def __unicode__(self):
        return self.user.get_full_name()
    

class Distro(models.Model):
    nama = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="logo")
    keterangan = models.TextField()
    url = models.URLField(null=True, blank=True)
    
    def get_logo(self):
        static_url = settings.STATIC_URL
        return safe("<img width='100' src='%s%s'/>"%(static_url, self.logo.url) )
    
    
    def __unicode__(self):
        return self.nama

class TemplateOS(models.Model):
    file_path = models.TextField()
    min_memory = models.IntegerField()
    
    def __unicode__(self):
        return "aa"

class Version(models.Model):
    version = models.CharField(max_length=255)
    distro = models.ForeignKey(Distro)
    templateos = models.ForeignKey(TemplateOS)
    aktif = models.BooleanField()
    
    def __unicode__(self):
        return "%s %s" % (self.distro.nama, self.version)

class Pesan(models.Model):
    user = models.ForeignKey(User)
    pesan = models.TextField()
    tgl_pesan = models.DateTimeField(auto_now_add=True)
    sudah_baca = models.BooleanField()
    
    def __unicode__(self ):
        return self.pesan
