__author__ = 'zbnoah2811'

from django import forms
from models import Shapefiler

class Registration(forms.Form):
    username = forms.CharField(label='Username', required=True)
    email = forms.CharField(label='Email', required=True)
    password = forms.CharField(label='Password', required=True,widget=forms.PasswordInput)


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=255)
    file = forms.FileField()

class StyleField(forms.Form):
    attribute = forms.ChoiceField()
    fillClr = forms.ChoiceField()
    weight = forms.ChoiceField()
    color = forms.ChoiceField()
    dashArray = forms.ChoiceField()
    fillOpac = forms.ChoiceField()