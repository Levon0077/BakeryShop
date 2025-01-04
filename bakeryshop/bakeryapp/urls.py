from django.urls import path

from .views import shop_index

app_name = 'bakeryapp'

urlpatterns = [
    path('', shop_index, name='shop_index')
]