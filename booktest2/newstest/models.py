from django.db import models

# Create your models here.
class TypeInfo(models.Model):
    tname = models.CharField(max_length=20)

class NewInfo(models.Model):
    ntitle = models.CharField(max_length=60)
    ncontent = models.TextField()
    npub_date = models.DateTimeField()
    ntype = models.ManyToManyField('TypeInfo')

