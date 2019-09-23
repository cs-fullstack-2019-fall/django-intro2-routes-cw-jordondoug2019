from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gogetthegood/', views.gogetthegood, name='gogetthegood'),
    path('happyhappyjoyjoy/', views.happyhappyjoyjoy, name='happyhappyjoyjoy'),
    path('youheard/<str:words>', views.youheard, name='youheard')

]