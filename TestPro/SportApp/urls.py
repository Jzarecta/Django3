from django.urls import path
from .views import Sport, Home, contact

urlpatterns = [
    path('', Home, name = "home"),
    path('sports/', Sport, name = "sports"),
    path('contact/', contact, name='contact'),
    ]
