from django.shortcuts import render
from django.http import HttpResponse
from Django_Introduction.tasks.models import Task

# Create your views here.
def index(request):
    return HttpResponse('Nice work!')

def list_tasks(request):
    all_tasks = Task.objects.all()

    return HttpResponse(f"{t.id}|{t.task_title} - {t.task_text}" for t in all_tasks)

def list_tasks_template(request):
    context = {
        "task": "description",
        "dynamic_tasks": Task.objects.all()
    }
    return render(request, "tasks.html", context)