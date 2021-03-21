from django.urls import path
from upskill_photography import views

app_name = 'upskill_photography'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('discovery/', views.discovery, name='discovery'),
    path('categories/', views.categories, name='categories'),
    path('categories/nature/', views.nature, name='nature'),
    path('categories/people/', views.people, name='people'),
    path('categories/architecture/', views.architecture, name='architecture'),
    path('categories/astronomy/', views.astronomy, name='astronomy'),
    path('search/', views.search_result, name='search_result'),
    path('account/', views.account, name='account'),
    path('account/uploads', views.uploads, name='uploads'),
]
