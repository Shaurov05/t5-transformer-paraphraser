from django import forms
from crispy_forms.helper import FormHelper 
from crispy_forms.layout import Layout, Submit 
 

class ParaphraseForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'text',
            Submit('submit', 'Paraphrase', css_class='btn-success')
        )

