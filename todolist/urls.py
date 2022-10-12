import imp
from todolist.views import create_task, update_task
from django.urls import path
from todolist.views import show_todolist
from todolist.views import register #sesuaikan dengan nama fungsi yang dibuat
from todolist.views import login_user #sesuaikan dengan nama fungsi yang dibuat
from todolist.views import logout_user #sesuaikan dengan nama fungsi yang dibuat
from todolist.views import add_task
from todolist.views import delete
from todolist.views import show_json
app_name = 'todolist'


urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('create_task/', create_task, name='create_task'),
    path('update/<int:pk>', update_task, name='update_task'),
    path('delete/<int:pk>', delete, name='delete'),
    path('logout/', logout_user, name='logout'),
    path('json/', show_json, name='show_json'),
    path('add/', add_task, name='add_task'),
]