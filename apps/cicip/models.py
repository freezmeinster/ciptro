from django.db import models

class Distro(models.Model):
    nama = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="assets/logo")
    keterangan = models.TextField()
    
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
    
    def __unicode__(self):
        return "%s %s" % (self.distro.nama, self.version)
