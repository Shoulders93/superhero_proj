from django.urls import path
from django.urls.resolvers import URLPattern

from .import views

app_name = 'superheroes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:hero_id>/', views.detail, name='detail'),
    path('new/', views.create, name='create'),
    path('delete/<int:hero_id_delete>/', views.delete, name ='delete'),
    path('edit/', views.create, name= 'edit'),
]