from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
# Create your views here.
def todo_home(request):
    return HttpResponse("this is todo home page !!!") 
def hello(request): 
    return HttpResponse("this is hello page!!!")
@login_required
def hello_protected(request): 
    return HttpResponse("this is hello protected page!!!")

def register(request): 
    form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})