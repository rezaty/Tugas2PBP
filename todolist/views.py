from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from todolist.forms import TaskForm
from todolist.models import Task

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    todo = Task.objects.all()
    context = {
    'nama': 'Reza Taufiq Yahya',
    'NPM': '2106654183',
    'todolist' : todo
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

def create_task(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            todo = Task(
                title=request.POST.get("title"),
                description=request.POST.get("description"),
                date = datetime.now(),
                user = request.user
            )
            todo.save()
            return redirect('todolist:show_todolist')
    else :
        form = TaskForm()
    context = {'form':form}
    return render(request, 'create_task.html', context)

def set_task(request, pk):
    todolist = Task.objects.filter(pk=pk)
    if todolist.get().is_finished:
        todolist.update(is_finished=False)
    else:
        todolist.update(is_finished=True)
    return redirect('todolist:show_todolist')

def delete(request, pk):
    todolist = Task.objects.filter(pk=pk)
    todolist.delete()
    return redirect('todolist:show_todolist')
