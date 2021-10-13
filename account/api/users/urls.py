from django.urls import path, include
from django.contrib import admin


from .views import UserDetailAPIView

app_name='user'

urlpatterns = [
    path('<int:id>/', UserDetailAPIView.as_view(), name='detail'),
    # path('<username>/questions/', UserQuestionAPIView.as_view(), name='question-list'),

]