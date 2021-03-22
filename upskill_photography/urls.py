from django.urls import path
from upskill_photography import views

app_name = 'upskill_photography'

urlpatterns = [
    path('upload', views.upload, name='upload'),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('discovery/', views.discovery, name='discovery'),
    path('categories/', views.categories, name='categories'),
    path('categories/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('search/', views.search_result, name='search_result'),
    path('account/', views.account, name='account'),
    path('account/uploads', views.uploads, name='uploads'),
]
