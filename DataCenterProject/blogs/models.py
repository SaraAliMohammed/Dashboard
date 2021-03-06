from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
from django.core.urlresolvers import reverse

def validate_server(name):
    if name =="":
        raise ValidationError("Please enter name.")
class Server(models.Model):
    typeChoices = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
    )

    name=models.CharField(max_length=30,primary_key=True,default='UnKnown',validators=[validate_server])
    Type = models.CharField(max_length=1, choices = typeChoices)
    RAM = models.CharField(max_length=30)
    Core = models.PositiveSmallIntegerField()
    Storage = models.CharField(max_length=30)
    RackNum = models.ForeignKey('Rack', related_name='racs')

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('server_edit', kwargs={'pk': self.pk})

class Mac(models.Model):
    ServerID = models.ForeignKey('Server', related_name='macs')
    MacNum = models.CharField(max_length = 30)

class Rack(models.Model):
    RackNum = models.PositiveSmallIntegerField(primary_key=True)

    #in admin to display racs num in add server dropdown list
    def __str__(self):
        return str(self.RackNum)






