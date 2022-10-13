from django.urls import path
from todolist.views import logout_user, show_todolist, register, login_user, get_task, update_task, delete_task, show_json
from todolist.views import add_task
app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', get_task, name='create-task'),
    path('update-task/<str:pk>/', update_task, name='update-task'),
    path('delete-task/<str:pk>/', delete_task, name='delete-task'),
    path('json/', show_json, name='show_json'),
    path('add/', add_task, name='add'),
]