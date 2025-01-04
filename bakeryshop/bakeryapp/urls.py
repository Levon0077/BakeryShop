from django.urls import path

from .views import shop_index

app_name = 'bakeryshop'

urlpatterns = [
    path('', shop_index, name='shop_index')
]