from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "title": "I am the title"
    }
    return render(request, "html/index.html", context=context)