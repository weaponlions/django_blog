from django.shortcuts import render
from django.contrib import messages
# Create your views here.

def index(request):
    messages.add_message(request, messages.SUCCESS, 'OK YOU WIN')
    return render(request, 'app4/main.html')


def message(request):
    messages.info(request, 'Ok YOU WIN')
    return render(request, 'app4/main.html')