from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('meetings/<int:id>/', views.meeting_detail, name="detail"),
    path('meetings/new/', views.create_meeting, name="create_meeting"),
]
