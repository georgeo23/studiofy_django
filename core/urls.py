from django.urls import path

from .views import current_user, UserList, CoversSet

urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    path('covers/', CoversSet.as_view())
]