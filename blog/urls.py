from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('accounts/register/', views.register, name='register'),
    path('login', views.login, name='login '),
    path('blog/<int:post_id>/', views.blog, name='blog'),
   

]
