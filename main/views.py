from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main(request):
    return render(request, 'main.html')


def info(request):
    return render(request, 'info1.html')

def bucket(request):
    return render(request, 'bucket.html')
