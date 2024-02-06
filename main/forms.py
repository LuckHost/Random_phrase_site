from django import forms

class MainpageCheckbox(forms.ModelForm):
    is_funny = forms.BooleanField()