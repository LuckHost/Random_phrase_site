from django import forms
from .models import Checkbox

class MainpageCheckbox(forms.Form):
    
    class Meta:
        model = Checkbox
        
    def __init__(self, *args, **kwargs):
        super(MainpageCheckbox, self).__init__(*args, **kwargs)
        self.fields['is_funny'] = forms.BooleanField(required=False, 
                    widget=forms.CheckboxInput(attrs={'name': 'is_funny',
                                                      'value': 'funny'}))
        self.fields['is_animals'] = forms.BooleanField(required=False, 
                    widget=forms.CheckboxInput(attrs={'name': 'is_funny',
                                                      'value': 'animal'}))