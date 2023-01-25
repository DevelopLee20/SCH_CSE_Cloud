from django.contrib.auth.models import User
from django.db import models
from .utils import *

class Content(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    file = models.FileField(upload_to=file_edit_name)
    create_date = models.DateTimeField()

    def __str__(self):
        text = str(self.create_date)[:10]
        return f'{text} {self.title}'