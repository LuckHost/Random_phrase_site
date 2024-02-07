from django import forms

class MainpageCheckbox(forms.Form):
    is_funny = forms.BooleanField(required=False)