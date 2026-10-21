from rest_framework import permissions


class IsModer(permissions.BasePermission):
    def has_permission(self, request, view):

        if not request.user.is_authenticated:
            return False

        if request.user.groups.filter(name='moderators').exists():
            return True
        return False

