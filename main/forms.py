from django import forms
from .models import Checkbox

class MainpageCheckbox(forms.Form):
    is_funny = forms.BooleanField(required=False)
    
    class Meta:
        model = Checkbox
        
    def __init__(self, *args, **kwargs):
        super(MainpageCheckbox, self).__init__(*args, **kwargs)
        self.fields['is_funny'] = forms.BooleanField(initial=True, required=False, 
                    widget=forms.CheckboxInput(attrs={'id': 'животные', 'name': 'бегемот', 'value': 'бегемот'}))