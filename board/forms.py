from django import forms
from django.forms import ModelForm
from .models import Message

class BoardForm(forms.Form):
    text = forms.CharField(label='メッセージ', max_length=100)
