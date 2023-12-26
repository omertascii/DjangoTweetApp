from django import forms
from . import forms

class AddTweetForm(forms.Form):
    username_input = forms.CharField(label="Username",max_length=50)
    message_input = forms.CharField(labe="Message",max_length=100)