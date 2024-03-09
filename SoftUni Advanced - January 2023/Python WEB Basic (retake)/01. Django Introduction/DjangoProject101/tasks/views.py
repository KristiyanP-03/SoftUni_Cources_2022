from django import http
from tasks.models import Task
from django.shortcuts import render


# Create your views here.
def index(request):
    return http.HttpResponse("It works!")


def task_tab(request):
    all_tasks = Task.objects.all()
    result = ', '.join(f'{t.title}({t.id})' for t in all_tasks)
    return http.HttpResponse(result)


def working_template(request):
    all_tasks = Task.objects.all()

    context = {
        "info": "This is pre-alpha project!",
        "tasks": all_tasks
    }
    return render(request, "index.html", context)
