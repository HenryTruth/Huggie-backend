from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from .views import MyRequestsView

app_name = 'profile'
router = DefaultRouter(trailing_slash=False)

router.register("contact", MyRequestsView)




urlpatterns = [
    path("", include(router.urls))
    # path('',ContactView.as_view(), name='contact-list'),
    # path('<int:id>/',ContactAPIDetailView.as_view(), name='contact')

]