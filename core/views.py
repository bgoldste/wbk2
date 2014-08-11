# Create your views here.

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from forms import EmailForm
from django import forms
from core.models import Subscriber
from django.contrib.messages.views import SuccessMessageMixin

class HomePageView(SuccessMessageMixin, CreateView):
    template_name = "index.html"
    form_class = EmailForm
    model = Subscriber
    success_url = '/#signup'
    success_message = "Thanks for being a part of Wavebook. We'll be in touch soon."
  
    def get_success_message(self, cleaned_data):
        return self.success_message 

