from django.urls import path
from . import views
from shopApp.views import about, form_comment, form_contact
from .views import about 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', about, name='about'),
    path('form_comment/', form_comment, name='form_comment'),
    path('form_contact/', form_contact, name='form_contact'),
]
