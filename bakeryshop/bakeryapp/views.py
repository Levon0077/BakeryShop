from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def shop_index(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Hello dear visitor!')