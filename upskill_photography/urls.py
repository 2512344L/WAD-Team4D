from django.urls import path
from upskill_photography import views

app_name = 'upskill_photography'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('category/', views.show_category, name='show_category'),
    path('discovery/', views.discovery, name='discovery'),
    path('Astronomy/', views.show_category, name='Astronomy'),
    path('People/', views.show_category, name='People'),
    path('Architecture/', views.show_category, name='Architecture'),
    path('Uploads/', views.uploads, name="uploads"),
    path('Account/', views.account, name="account"),
    path('FAQ/', views.FAQ, name="FAQ"),
    path('contact/', views.contact, name="contact"),
]
