from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_image, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('upload/', views.upload_image, name='upload'),
]