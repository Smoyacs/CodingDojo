from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.contrib import messages

from acceso.models import Usuario
from acceso.forms import UsuarioForm
from acceso.forms import LoginForm

import bcrypt
# Create your views here.


class LoginView(View):
    
    def get(self, request):

        if 'usuario' in request.session:
            messages.error(request, 'YA ESTAS LOGEADO. Si quieres salir, CLICK EN SALIR!!')
            return redirect('/')

        contexto = {
            'formRegister': UsuarioForm(),
            'formLogin': LoginForm()
        }

        return render(request, 'acceso/login.html', contexto)

    def post(self, request):
        print(request.POST)

        form = UsuarioForm(request.POST)

        if form.is_valid():
            
            usuario = form.save(commit=False)
            usuario.password = bcrypt.hashpw(usuario.password.encode(), bcrypt.gensalt()).decode()
            usuario.save()
            
            messages.success(request, 'Usuario creado correctamente')
            return redirect(reverse('acceso:acceso'))
        else:

            contexto = {
                'formRegister': form,
                'formLogin': LoginForm()
            }

            messages.error(request, 'Con errores, solucionar.')
            return render(request, 'acceso/login.html', contexto) 


def login(request):

    if request.method == 'POST':

        form = LoginForm(request.POST)

        if form.is_valid():
            
            user = Usuario.objects.filter(email=form.cleaned_data['email']).first()
            if user:
                form_password = form.cleaned_data['password']
                if bcrypt.checkpw(form_password.encode(), user.password.encode()):
                    
                    request.session['usuario'] = { 'first_name' : user.first_name, 'last_name' : user.last_name, 'email' : user.email, 'id': user.id }
                    return redirect('/')
                else:
                    messages.error(request, 'Contraseña o Email o Nombre de Usuario INCORRECTO')
            else:
                messages.error(request, 'Contraseña o Email o Nombre de Usuario INCORRECTO')

            return redirect(reverse('core:menu'))
        else:
            contexto = {
                'formRegister': UsuarioForm(),
                'formLogin': form
            }
            return render(request, 'acceso/login.html', contexto) 

def logout(request):

    if 'usuario' in request.session:
        messages.success(request, 'SALISTE')
        del request.session['usuario']
    else:
        messages.error(request, 'No estas logeado.')

    return redirect(reverse('acceso:acceso'))