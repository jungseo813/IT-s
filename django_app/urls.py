from . import views
from django.urls import path

urlpatterns = [
    path('',views.login_view, name='login'),
    path('join/', views.join_view, name='join'),
]