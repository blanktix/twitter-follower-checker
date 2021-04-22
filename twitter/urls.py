from django.urls import path
from . import views

urlpatterns = [
    path('followers/<str:nama>/',views.daftar_follower),
    path('following/<str:nama>/',views.daftar_following),
    path('following-not-followers/<str:nama>/',views.daftar_following_not_followers),
]
