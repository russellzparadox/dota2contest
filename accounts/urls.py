# urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('user-info/', views.user_info, name='user_info'),
    path('', views.index, name='index'),
    path('complete_profile', views.complete_profile, name='complete_profile'),
    path('logout/', views.logout_view, name='logout'),  # Add the logout URL pattern

    # Add other URLs as needed
]
