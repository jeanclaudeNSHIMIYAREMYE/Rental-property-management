from rest_framework.permissions import BasePermission

class IsOwnerRole(BasePermission):
    
     message=("Seuls les proprietaire peuvent gerer les logements")
     
     def has_permission(self, request, view):
          return(
              request.user,
              request.user.is_authenticated and request.user.role=="OWNER"
          )