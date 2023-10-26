from django.urls import path
from .views import item_form, success 

urlpatterns = [
    path('', item_form, name='item-form'),
    path('success/', success, name='success'),
    path('icecream/add/', item_form, name='add-icecream'),
]