from django.shortcuts import redirect, render, HttpResponse

# Create your views here.
# http://127.0.0.1:8000/blogs

def root(request):
    return redirect('/blogs')

def index(request):
    return HttpResponse("placeholder para luego mostrar una lista de todos los blogs")

def new(request):
    return HttpResponse("placeholder para mostrar un nuevo formulario para crear un nuevo blog")

def create(request):
    return redirect("/")

def show(request, number):
    return HttpResponse(f"placeholder para mostrar el blog numero: {number}"")

def edit(request, number):
    return HttpResponse(f"placeholder para editar el blog {number}")
    
def destroy(request, number):
    return redirect("/")

