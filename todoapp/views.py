from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from django.contrib.auth import login



# Create your views here.
def todo_home(request):
    return HttpResponse("this is todo home page !!!") 
def hello(request): 
    return HttpResponse("this is hello page!!!")
@login_required
def hello_protected(request): 
    return HttpResponse("this is hello protected page!!!")

def register(request): 
    if request.method == 'POST': 
        form = UserRegistrationForm(request.POST)
        if form.is_valid(): 
            user = form.save()
            login(request,user)
            return redirect('hello_protected')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})