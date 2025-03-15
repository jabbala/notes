from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'user':'Gunasekar', 'today': datetime.today()}


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'
