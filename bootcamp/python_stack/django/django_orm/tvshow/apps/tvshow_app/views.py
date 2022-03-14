from multiprocessing import context
from django.views import View
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse

from apps.tvshow_app.models import Show
from apps.tvshow_app.forms import ShowForm

# Create your views here.

def To_shows(request):
    return redirect(reverse('tvshow_app:show_list'))


def ShowList(request):
    
    context ={
        "all_show":Show.objects.all()
    }
    
    return render(request, "tvshow_app/list_show.html", context)




def ShowCreate(request):
    
    if request.method == 'GET':
        context = {
            'form': ShowForm()
        }
        return render(request, 'tvshow_app/create_show.html', context)
    
    else:
        form = ShowForm(request.POST)
        if form.is_valid():
            
            form.save()
            messages.success(request, 'Show Creado')
            return redirect(reverse('tvshow_app:show_list'))
        else:
            context = {
                'form': form,
            }
            messages.error(request, 'El formulario tiene errores')
            return render(request, 'tvshow_app/create_show.html', context) 


def ShowUpdate(request, id):
    
    if request.method == 'GET':
        show = Show.objects.get(id=id)
        context = {
            'form': ShowForm(instance=show), 
        }
        return render(request, 'tvshow_app/edit_show.html', context)
    
    else:
        show = Show.objects.get(id=id)
        
        form = ShowForm(request.POST, instance=show)
        if form.is_valid():
            form.save()
            messages.success(request, 'Show Editado')
            return redirect(reverse('tvshow_app:show_list'))
        else:

            contexto = {
                'form': form, 
            }

            messages.error(request, 'El formulario tiene errores')
            return render(request, 'tvshow_app/edit_show.html', contexto)


    
def ShowDetail(request, id):

    context = { 
        'show' : Show.objects.get(id=id)
    }
    return render(request, 'tvshow_app/detail_show.html', context)


def ShowDelete(request, id):
    
    show = Show.objects.get(id=id)
    show.delete()
    messages.success(request, 'Show eliminado')
    return redirect('/')