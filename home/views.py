from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home/welcome.html', {'user':'Gunasekar', 'today': datetime.today()})

@login_required(login_url='/admin')
def authorized(request):
    return render(request, 'home/authorized.html', {})