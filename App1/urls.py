from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='home'),
    path('contact', views.contact, name='contact'),
    path('save', views.save, name='save'),
    path('about', views.about, name='about'),
    path('products', views.products, name='products'),
]