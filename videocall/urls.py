from django.urls import path
from . import views

urlpatterns = [
   path("video-call/", views.video_call_view, name="video-call"),
    path('get-token/', views.get_token, name='get_token'),
]
