from rest_framework import permissions


class AuthPermission(permissions.BasePermission):
    perms = None

    def has_permission(self, request, view):
        if not request.user or (
            not request.user.is_authenticated and self.authenticated_users_only
        ):
            return False

        return request.user.has_perms([self.perms])
