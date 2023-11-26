from django import forms

class KeyChainInputForm(forms.Form):
    name = forms.CharField(label="Your name", max_length=100)