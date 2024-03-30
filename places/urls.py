from django.urls import path
from .views import places_page, haqida,landing,AddCommentView

app_name = 'places'
urlpatterns = [
    path('places/', places_page, name='places_page'),
    path('haqida/<int:id>/', haqida, name='haqida_page'),  
    path('landing/', landing, name='landing_page'),  
    path('add_comment/<int:id>/',AddCommentView.as_view(), name='add_comment'),  
]
