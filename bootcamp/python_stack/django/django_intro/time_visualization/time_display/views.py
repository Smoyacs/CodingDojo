from django.shortcuts import render
from datetime import datetime
    
def index(request):
    current_time = datetime.now().time()
    return render(request, 'index.html',{'current_time':current_time})