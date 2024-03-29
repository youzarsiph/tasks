""" Permissions """


from rest_framework.permissions import BasePermission


# Create your permissions here.
class IsOwner(BasePermission):
    """Allow the owner only"""

    def has_object_permission(self, request, view, obj):
        """Owners only"""

        return obj.user == request.user
