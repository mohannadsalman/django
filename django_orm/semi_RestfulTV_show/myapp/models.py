from django.db import models 

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=55)
    releasedate=models.DateField()
    desc = models.TextField()
    
