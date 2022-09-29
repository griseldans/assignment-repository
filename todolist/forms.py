from django import forms
from todolist.models import ToDoList

class TaskForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ['title', 'description']

# class UpdateTask(forms.ModelForm):
#     class Meta:
#         model = ToDoList
#         fields = ['is_finished']
