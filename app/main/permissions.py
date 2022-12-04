from rest_framework.permissions import IsAdminUser, SAFE_METHODS

class IsAdminUserOrReadOnly(IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super(
            IsAdminUserOrReadOnly, 
            self).has_permission(request, view)
        # Python3: is_admin = super().has_permission(request, view)
        return request.method in SAFE_METHODS or is_admin