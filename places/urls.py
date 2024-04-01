from django.urls import path
from .views import places_page, about,landing,AddCommentView

app_name = 'places'
urlpatterns = [
    path('places/', places_page, name='places_page'),
    path('about/<int:id>/', about, name='about_page'),  
    path('landing/', landing, name='landing_page'),  
    path('add_comment/<int:id>/',AddCommentView.as_view(), name='add_comment'),  
]
