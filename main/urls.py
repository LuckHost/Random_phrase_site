from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('add_words', views.add_words, name='adding_page')
]
