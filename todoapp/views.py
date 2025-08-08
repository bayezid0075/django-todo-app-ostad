from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, TaskForm
from django.contrib.auth import login
from .models import Task

# Create your views here.
def todo_home(request):
    return HttpResponse("this is todo home page !!!") 

def hello(request): 
    return HttpResponse("this is hello page!!!")

@login_required
def hello_protected(request): 
    user = request.user
    return render(request, 'protected.html', {'user': user})

def register(request): 
    if request.method == 'POST': 
        form = UserRegistrationForm(request.POST)
        if form.is_valid(): 
            user = form.save()
            print(user, 'userdata')
            login(request,user)
            return redirect('hello_protected')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def task_list(request): 
    tasks = Task.objects.filter(user= request.user)
    return render(request, 'task_list.html', {'tasks': tasks})

@login_required
def create_task(request): 
    if request.method  == 'POST': 
       form = TaskForm(request.POST)
       if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user 
            task.save()
            return redirect('tasklist')

    form = TaskForm()
    return render(request, 'create_task.html', {'form': form})

@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasklist')
    else:
        form = TaskForm(instance=task)
    return render(request, 'create_task.html', {'form': form})


@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
    return redirect('tasklist')