from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404

# Create your views here.
def index(request):
    return HttpResponse('index is working')


def redirecting(request):
    return redirect('https://www.google.com/')


def id_maker(request, id):
    map = {
        1: 'DevOps',
        2: 'QA'
    }
    place = f"{map.get(id, 'None')}"

    return HttpResponse(f"Department[ id: {id}] is '{place}' ")


def template_view(request, id):
    map = {
        1: 'DevOps',
        2: 'QA'
    }
    place = f"{map.get(id, 'None')}"

    return render(request, 'departments/details.html')


def error_page(request, id):
    return HttpResponse('ERROR404')