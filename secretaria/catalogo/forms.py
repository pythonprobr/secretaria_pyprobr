from django import forms

class EmailForm(forms.Form):
    name = forms.EmailField()
