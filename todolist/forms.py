from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(label='title', max_length=255)
    description = forms.CharField(label='description', max_length=255)