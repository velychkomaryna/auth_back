from django.urls import path

from . import views

urlpatterns = [
    path('private/', views.PrivateView.as_view(), name='private'),
]
