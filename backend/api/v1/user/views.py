from rest_framework import generics

from api.v1.user.filters import UserFilter
from api.v1.user.permissions import UserPermission
from api.v1.user.serializers import (
    UserListCreateSerializer,
    UserDetailUpdateSerializer,
    UserCountSerializer,
)
from app.user.models import User


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserListCreateSerializer
    permission_classes = [UserPermission]
    filterset_class = UserFilter


class UserDetailUpdateView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailUpdateSerializer
    permission_classes = [UserPermission]


class UserCountView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserCountSerializer

    def get_object(self):
        return {"count": self.queryset.count()}
