from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,DeleteView
from django.views.generic import TemplateView
from .models import Sendmessage


from . import forms
# Create your views here.

class Signup(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name= 'basicapp/signup.html'

class Sendmess(CreateView):
    form_class=forms.Sendmessage
    success_url=reverse_lazy('login')
    template_name='basicapp/send.html'


def inbox(request):
    user = request.user
    out = Sendmessage.objects.filter(username=user).order_by('-date')

    return render(request,'basicapp/rece.html',{'out':out[:]})
