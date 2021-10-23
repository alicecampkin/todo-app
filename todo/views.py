from django.http import HttpResponse
from django.shortcuts import render

from .models import Todo

# Create your views here.

def list_todos(request):
    """ Displays a list of posts """

    todos = Todo.objects.filter(completed=False).order_by('-created_on')

    context = {
        'page_title': 'To Do List',
        'todos': todos
    }

    return render(request, 'index.html', context)