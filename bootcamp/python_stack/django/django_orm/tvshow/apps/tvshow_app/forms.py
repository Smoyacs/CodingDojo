
from datetime import date
from django import forms
from apps.tvshow_app.models import Show


class ShowForm(forms.ModelForm):
    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 2:
            raise forms.ValidationError('Titulo no puede ser menor a 4 caracteres')
        return title
    
    def clean_network(self):
        network = self.cleaned_data.get('network')
        if len(network) < 3:
            raise forms.ValidationError('Network no puede ser menor a 3 caracteres')
        return network
    
    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 10:
            raise forms.ValidationError('Descripcion no puede ser menor a 10 caracteres')
        return description
    
    def clean_release_date(self):
        release_date = self.cleaned_data['release_date']


        if release_date > date.today():
            raise forms.ValidationError(
                    f"solo fechas en pasado."
                )
        return release_date
    
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
            'release_date': forms.DateInput(attrs={'class': 'form-control' , 'type':'date', 'max':date.today().strftime('%Y-%m-%d')}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }