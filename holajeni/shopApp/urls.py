from django.urls import path
from . import views
from shopApp.views import about
from .views import about 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', about, name='about'),
]
