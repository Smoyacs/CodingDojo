from datetime import date

from django import forms

from acceso.models import Usuario



EDAD_REQUERIDA = 13

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))



class UsuarioForm(forms.ModelForm):
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if len(first_name) < 2:
            raise forms.ValidationError('first name no puede ser menor a 2 caracteres')
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if len(last_name) < 2:
            raise forms.ValidationError('last name no puede ser menor a 2 caracteres')
        return last_name

    def clean_birthday(self):
        birthday = self.cleaned_data['birthday']
        edad = calculate_age(birthday)

        if birthday > date.today():
            raise forms.ValidationError(
                    f"solo fechas en pasado."
                )

        if edad < EDAD_REQUERIDA:
            raise forms.ValidationError(
                    f"La edad es menor a {EDAD_REQUERIDA}, porque tiene {edad} años."
                )
        return birthday

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError('La contraseña no puede ser menor a 8 caracteres')
        return password
            


    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)

        if cleaned_data.get('password') != cleaned_data.get('confirmar_password'):
            raise forms.ValidationError(
                    "Las contraseñas no coinciden"
                )

    class Meta:
        model = Usuario
        fields  = ['first_name','last_name','email','password', 'confirmar_password', 'birthday']

        labels = {
            'first_name':'First Name: ',
            'last_name':'Last Name: ',
            'email':'Email: ',
            'password':'Password: ',
            'confirmar_password':'Confirm Password: ',
            'birthday': 'Date of Birth',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'type':'email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'confirmar_password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control', 'type':'date', 'max':date.today().strftime('%Y-%m-%d')}),
        }

class LoginForm(forms.Form):
    email = forms.CharField(
                    label='Email', 
                    max_length=50, 
                    required=True, 
                    widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email@ejemplo.com'})
                )

    password = forms.CharField(
                    label='Contraseña', 
                    required=True, 
                    widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Contraseña'})
                )