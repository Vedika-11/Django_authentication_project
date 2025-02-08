from django.urls import path
from .views import *

urlpatterns=[
    path('signup/',signup_view , name='signup'),
    path('login/' ,login_view , name='login'),
    path('logout/' , logout_view , name='logout'),
    path('dashboard/' , dashboard_view , name='dashboard'),
    path('profile/' , profile_view , name='profile'),
    path('change-password/', change_password_view , name='change-password'),

]