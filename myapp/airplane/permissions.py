from rest_framework.permissions import BasePermission

class IsPilot(BasePermission):
    message = "only pilot can do"
    def has_permission(self, request, view):
        return hasattr(request.user , 'pilot')