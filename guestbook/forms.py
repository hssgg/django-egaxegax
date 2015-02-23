from django import forms
from django.utils.translation import ugettext as _
from guestbook.models import *

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Greeting
        exclude = ['author', 'subject', 'date']
        widgets = {
            'title': forms.TextInput(attrs={'style': 'width: 90%'}),
            'content': forms.Textarea(attrs={'rows': 10}),
        }

class AddSubjForm(forms.ModelForm):
    class Meta:
        model = Greeting_Subject
        exclude = ['count']
        widgets = {
            'subject': forms.TextInput(attrs={'style': 'width: 90%'}),
        }
