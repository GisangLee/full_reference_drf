from django.urls import path

from api.v1.user.views import (
    UserListCreateView,
    UserDetailUpdateView,
    UserCountView,
)

urlpatterns = [
    path("", UserListCreateView.as_view()),
    path("<int:pk>/", UserDetailUpdateView.as_view()),
    path("count/", UserCountView.as_view()),
    # add etc action view
]
