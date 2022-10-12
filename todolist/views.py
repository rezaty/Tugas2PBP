from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from todolist.forms import TaskForm
from todolist.models import Task
from django.core import serializers

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    todo = Task.objects.filter(user=request.user)
    context = {
    'nama': 'Reza Taufiq Yahya',
    'NPM': '2106654183',
    'todolist' : todo,
    }
    return render(request, "todolist.html", context)


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
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    return response

@login_required(login_url='/todolist/login/')
def create_task(request):
    if request.method == 'POST':
        task = Task()
        task.user = request.user
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.save()
        return redirect('todolist:show_todolist')

    return render(request, 'createtask.html')

@login_required(login_url='/todolist/login/')
def show_json(request):
    orang = request.user
    dataTask = Task.objects.all().filter(user = orang)
    return HttpResponse(serializers.serialize("json", dataTask), content_type="application/json")

def add_task(request):
    if request.method == 'POST':
        task = Task()
        task.user = request.user
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.save()    
    return redirect('todolist:show_todolist')

def delete(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('todolist:show_todolist')

def update_task(request, pk):
    task = Task.objects.get(pk=pk)
    if (task.is_finished == True):
        task.is_finished = False
    else:
        task.is_finished = True
    task.save()
    return redirect('todolist:show_todolist')

