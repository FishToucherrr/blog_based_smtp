from django.urls import path
from django.contrib import admin
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:pk>/', views.detail, name='detail'),
    path('archives/<int:year>/<int:month>/', views.archive, name='archive'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout',views.logout,name='logout'),
    path('categories/<int:pk>/', views.category, name='category'),
    path('tags/<int:pk>/', views.tag, name='tag'),
    path('blog/', views.blog, name='blog'),
    path('profile/<str:name>/', views.profile, name='profile'),
]