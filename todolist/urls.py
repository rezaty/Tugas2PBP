from todolist.views import create_task
from django.urls import path
from todolist.views import show_todolist
from todolist.views import register #sesuaikan dengan nama fungsi yang dibuat
from todolist.views import login_user #sesuaikan dengan nama fungsi yang dibuat
from todolist.views import logout_user #sesuaikan dengan nama fungsi yang dibuat
app_name = 'todolist'


urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('create-task/', create_task, name='create-task'),
    path('logout/', logout_user, name='logout'),
]