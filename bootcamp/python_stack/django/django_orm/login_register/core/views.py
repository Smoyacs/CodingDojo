from django.shortcuts import redirect, render
from django.urls import reverse

# Create your views here.

def index(request):
    return redirect(reverse('core:successfully'))

def success(request):
    return render(request, 'core/success.html')