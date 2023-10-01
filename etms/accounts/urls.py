
from . import views
from django.urls import path


urlpatterns = [
    path('Register/',views.Register,name='Register'),
    path('Login/',views.Login,name='Login')
]