from rest_framework.permissions import BasePermission, SAFE_METHODS


class MenuItemPermission(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user and request.user.is_authenticated


class IsBookingOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and obj.user_id == request.user.id
