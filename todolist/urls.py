import imp
from todolist.views import create_task
from django.urls import path
from todolist.views import show_todolist
from todolist.views import register #sesuaikan dengan nama fungsi yang dibuat
from todolist.views import login_user #sesuaikan dengan nama fungsi yang dibuat
from todolist.views import logout_user #sesuaikan dengan nama fungsi yang dibuat
from todolist.views import set_task
from todolist.views import delete
app_name = 'todolist'


urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('create_task/', create_task, name='create_task'),
    path('set_task/<int:pk>', set_task, name='set_task'),
    path('delete/<int:pk>', delete, name='delete'),
    path('logout/', logout_user, name='logout'),
]