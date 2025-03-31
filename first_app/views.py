from django.http import HttpResponse
from django.shortcuts import render


def django_greetings(request) -> HttpResponse:
    name = "Anatoli"
    return HttpResponse(
        "<h1>Greeting from the Django APP!!! :)</h1>"
    )

def user_greetings(request, name = "Anatoli"):
    # name = "Anatoli"
    return HttpResponse(
        f"<h1>Greeting, {name}!!! :)</h1>"
    )

def index_page(request):
    return render(request, 'my_html.html')

def user_hello(request, name):
    return HttpResponse(
        f"<h1>Hello, {name}!!! :)</h1>"
    )