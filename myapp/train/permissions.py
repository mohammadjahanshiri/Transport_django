from rest_framework.permissions import BasePermission

class IsDriver(BasePermission):
    message = "only driver can do"
    def has_permission(self, request, view):
        return hasattr(request.user , 'driver')