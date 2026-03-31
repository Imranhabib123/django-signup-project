from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup_view, name='signup'),
    path('success/', views.signup_success, name='signup_success'),
]
