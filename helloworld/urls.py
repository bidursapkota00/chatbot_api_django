from django.urls import path

from .views import HomePageView, Id, api

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('post/', api, name='write'),
    path('get/', Id.as_view(), name='read'),
]