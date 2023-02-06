from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserForm(UserCreationForm):
    student_number = forms.IntegerField(label="학번")

    class Meta:
        model = User
        fields = ("username", "student_number")