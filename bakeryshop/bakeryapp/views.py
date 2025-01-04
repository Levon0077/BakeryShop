from timeit import default_timer
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def shop_index(request: HttpRequest) -> HttpResponse:

    context = {
        'runtime':default_timer()
    }

    return render(request, 'bakeryapp/index.html', context=context)