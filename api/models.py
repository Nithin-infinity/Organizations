from django.db import models

# Create your models here.

class Organization(models.Model):
    domain = [
        ('Technology', 'Technology'),
        ('Education', 'Education'),
        ('Environment', 'Environment'),
        ('Humanities', 'Humanities'),
        ('Arts', 'Arts'),
        ('Business', 'Business'),
        ('Politics', 'Politics')
    ]
    name = models.CharField(max_length=50)
    dateEstablished = models.DateField()
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    country = models.CharField(max_length=25)
    domain = models.CharField(max_length = 50, choices = domain, default='Education')
    orgHead = models.CharField(max_length=25)
    numMembers = models.PositiveIntegerField()

    def __str__(self):
        return self.name