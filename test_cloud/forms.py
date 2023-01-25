from django import forms
from .models import Content

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'summary']
        labels = {
            'title': '제목',
            'summary': '내용',
        }