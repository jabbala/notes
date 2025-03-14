from django.shortcuts import render
from datetime import datetime
def home(request):
    return render(request, 'home/welcome.html', {'user':'Gunasekar', 'today': datetime.today()})