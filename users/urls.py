from django.urls import path
from .views import RegisterView,Loginview,Logoutview,Profileview,ProfileView,ResetPasswordView,UserView
app_name='users'

urlpatterns=[
    path('register/',RegisterView.as_view(),name='register'),
    path('login_page/', Loginview.as_view(),name='login_page'),
    path('logout_page/', Logoutview.as_view(),name='logout_page'),
    path('profile/', Profileview.as_view(),name='profile'),
    path('profile_view/', ProfileView.as_view(),name='profile_view'),
    path('reset_password/', ResetPasswordView.as_view(),name='reset_password'),
    path('list/', UserView.as_view(),name='list'),
    
]