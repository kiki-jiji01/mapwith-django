from rest_framework.permissions import BasePermission


class IsCountryOwner(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_object_permission(self, request, view, obj):
        country = obj
        return country.user == request.user