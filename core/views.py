# Create your views here.

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from forms import EmailForm
from django import forms
from core.models import Subscriber


class HomePageView(CreateView):
    template_name = "index.html"
    form_class = EmailForm
    model = Subscriber
    success_url = '/'
    success_message = "Email saved successfully"
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
       
        return super(HomePageView, self).form_valid(form)


