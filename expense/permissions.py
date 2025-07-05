from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied
from rest_framework import status


class IsOwnerOrSuperuser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or obj.user == request.user
