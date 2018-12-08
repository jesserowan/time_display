from django.shortcuts import render
from time import gmtime, strftime

def index(request):
    context = {
        "date": strftime("%A, %B %d %Y"),
        "time": strftime("%H:%M %p"),
        "timezone": strftime("%Z")
    }
    return render(request, 'myapp/index.html', context)