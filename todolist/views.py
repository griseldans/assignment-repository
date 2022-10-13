from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse

from todolist.forms import TaskForm

import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout

from django.contrib.auth import authenticate, login

from django.shortcuts import redirect
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
    model = ToDoList.objects.get(id=pk)

    if(model.is_finished == False):
        model.is_finished = True
    else:
        model.is_finished = False
    model.save()
    return redirect('todolist:show_todolist')


@login_required(login_url='/todolist/login/')
def delete_task(request, pk):
    ToDoList.objects.get(id=pk).delete()
    return(redirect('todolist:show_todolist'))
    
def show_json(request):
    data = ToDoList.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/todolist/login/')
@csrf_exempt
def add_task(request):
    form = TaskForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            newTask = ToDoList.objects.create(user=request.user,title=title, description=description)
            data = {
                "pk" : newTask.pk,
                "title" : newTask.title,
                "description" : newTask.description,
                "is_finished" : newTask.is_finished,
                "date" : newTask.date,

            }
            newTask.save()
        return JsonResponse(data)

