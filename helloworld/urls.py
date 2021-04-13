from django.urls import path

from .views import HomePageView, Api, Id

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('api/<pk>/', Api.as_view(), name='readwrite'),
    path('api/', Id.as_view(), name='read'),
]