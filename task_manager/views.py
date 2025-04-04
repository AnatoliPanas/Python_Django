from django.http import HttpResponse
from django.shortcuts import render

def user_hello1(request):
    return HttpResponse(
        f"<h1>Hello, Prog2!!! :)</h1>"
    )
