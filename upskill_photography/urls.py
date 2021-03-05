from django.urls import path
from upskill_photography import views

app_name = 'upskill_photography'

urlpatterns = [
    path('', views.index, name='index'),
]