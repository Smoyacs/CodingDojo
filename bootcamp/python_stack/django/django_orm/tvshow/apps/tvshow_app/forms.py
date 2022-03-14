from dataclasses import fields
from django import forms
from apps.tvshow_app.models import Show


class ShowForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = ['title','network','release_date','description']

        labels = {
            'title': 'Title',
            'network': 'Network',
            'release_date': 'Release Date',
            'description': 'Description',  
        }
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'network': forms.TextInput(attrs={'class': 'form-control'}),
            'release_date': forms.DateInput(attrs={'class': 'form-control' , 'type': 'date'}, format='%Y-%m-%d'),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }