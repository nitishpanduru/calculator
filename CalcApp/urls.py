from django.urls import path
from . import views

app_name = 'calc'

urlpatterns = [
    path('add/',views.add,name='add'),
]
