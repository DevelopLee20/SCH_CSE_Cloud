from django.db import models
from . utils import *
from django.contrib.auth.models import User

class Content(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    summary = models.TextField()
    file = models.FileField(upload_to=file_edit_name)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        text = str(self.create_date)[:10]
        return f'{text} {self.title}'

class new_Content(models.Model):
    file = models.FileField(upload_to=file_edit_name)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField()