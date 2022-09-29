from statistics import mode
from todolist.forms import TaskForm, UpdateTask

import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout

from django.contrib.auth import authenticate, login

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.shortcuts import render
from todolist.models import ToDoList

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = ToDoList.objects.filter(user=request.user)

    context = {
        'todolist' : data_todolist,
        'username' : request.user,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, 'todolist.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def get_task(request):
    form = TaskForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            tempsave = form.save(commit=False)
            tempsave.user = request.user
            form.save()
            return(redirect('todolist:show_todolist'))

    context = {'forms': form}
    return render(request, 'task.html', context)

@login_required(login_url='/todolist/login/')
def update_task(request, pk):
    model = get_object_or_404(ToDoList, id=pk)

    if request.method == "POST":
        if(model.is_finished == False):
            model.is_finished = True
        else:
            model.is_finished = False
        model.save()
        return(redirect('todolist:show_todolist'))

    context = {'model': model}
    return render(request, 'todolist.html', context)

@login_required(login_url='/todolist/login/')
def delete_task(request, pk):
    if request.methos == "POST":
        ToDoList.objects.get(id=pk).delete()
    return(redirect('todolist:show_todolist'))
    