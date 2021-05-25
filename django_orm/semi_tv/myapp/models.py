from django.contrib.messages.api import error
from django.db import models


class ShowManger(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        ds = datetime.datetime.now
        if len(postData['title']) < 2:
            errors["title"] = "title name should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "network  should be at least 3 characters"
        if postData['desc']:
            if len(postData['desc']) < 10:
                errors["desc"] = "description  should be at least 10 characters"   
        return errors
class Show(models.Model):
    title = models.CharField(max_length=45,unique=True)
    network = models.CharField(max_length=45)
    description = models.TextField(default=None, blank=True, null=True)
    release_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManger() 