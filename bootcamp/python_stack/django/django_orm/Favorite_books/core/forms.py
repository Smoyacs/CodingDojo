from django import forms

from core.models import Book

class BookForm(forms.ModelForm):

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 2:
            raise forms.ValidationError(
                'Titulo debe tener a lo menos 2 caracteres ')
        return title

    def clean_description(self):
        description = self.cleaned_data['description']
        if len(description) < 5:
            raise forms.ValidationError(
                'descripcion debe tener a lo menos 5 caracteres ')
        return description

    class Meta:
        model = Book
        fields = ['title', 'description']

        labels = {
            'title': 'Título: ',
            'description': 'Descripción: '
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            }