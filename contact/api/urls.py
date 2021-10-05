from django.contrib import admin
from django.urls import path

app_name = 'profile'

from .views import (
    ContactAPIView,
    # ContactAPIDetailView
)


urlpatterns = [
    path('',ContactAPIView.as_view(), name='contact-list'),
    # path('<int:id>/',ContactAPIDetailView.as_view(), name='contact')

]