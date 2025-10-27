from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

def users(request):
    return render(request, 'index.html')

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"