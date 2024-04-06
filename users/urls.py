from django.urls import path
from .views import (RegisterView,Loginview,Logoutview,
                    Profileview,ProfileView,ResetPasswordView,
                    UserView,SendFriendRequestView, MyNetworksView,
                    AcceptFriendRequestView, IgnoreFriendRequestView,
                    DeleteFromFriendsView)


app_name='users'

urlpatterns=[
    path('register/',RegisterView.as_view(),name='register'),
    path('login-page/', Loginview.as_view(),name='login-page'),
    path('logout-page/', Logoutview.as_view(),name='logout-page'),
    path('profile/', Profileview.as_view(),name='profile'),
    path('profile-view/', ProfileView.as_view(),name='profile-view'),
    path('reset-password/', ResetPasswordView.as_view(),name='reset-password'),
    path('list/', UserView.as_view(),name='list'),

    #users friend request logic
     path('send-request/<int:id>/', SendFriendRequestView.as_view(),name='send-request'),
     path('networks/', MyNetworksView.as_view(),name='networks'),
     path('accept-friend/<int:id>/', AcceptFriendRequestView.as_view(),name='accept-friend'),
     path('ignore-friend/<int:id>/', IgnoreFriendRequestView.as_view(),name='ignore-friend'),
     path('delete-friend/<int:id>/', DeleteFromFriendsView.as_view(),name='delete-friend'),

    
]