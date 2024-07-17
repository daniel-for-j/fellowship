from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('testimonies', views.testimonies, name='testimonies'),
    path('about', views.about, name='about'),
    path('bhusf-messages', views.messages, name='messages'),
    path ('events', views.events, name = 'events'),
    path ('events/<slug:slug>/', views.eventDetails, name = 'eventDetails'),
    path ('testimony/<slug:slug>/', views.testimonyDetails, name='testimonyDetails')

]