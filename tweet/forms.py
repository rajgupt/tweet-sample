from django import forms
from .models import handle, message

class TweetForm(forms.Form):
    user = forms.CharField(max_length=100)
    message = forms.CharField(max_length=256)

        


