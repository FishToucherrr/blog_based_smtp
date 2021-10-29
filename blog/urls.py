from django.urls import path
from django.contrib import admin
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.mail, name='mail'),
    path('mail/',views.mail,name='mail'),
    path('sent/', views.sent, name='sent'),
    path('drafts/', views.drafts, name='drafts'),
    path('edit/<int:pk>/', views.edit, name='edit'),
]