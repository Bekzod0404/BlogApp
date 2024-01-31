from django.contrib.auth import admin

from Bekzod import views
from django.urls import path

from Bekzod.views import post_detail

app_name = 'Bekzod'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('post_confirm_delete/', views.PostConfirmDeleteView.as_view(), name='post-confirm-delete'),
    path('post_detail/', views.PostDetailView.as_view(), name='post-detail'),
    path('post_form/', views.PostFormView.as_view(), name='post-form'),
    path('user_posts/', views.UserPostsView.as_view(), name='user-posts'),
]
