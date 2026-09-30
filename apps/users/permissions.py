from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user,
            request.user.is_authenticated,
            request.user.role=="ADMIN"
            
        )
 
    
class IsOwner(BasePermission):
    def has_permission(self, request, view):
        return (
            
            request.user,
            request.user.is_authenticated,
            request.user.role=="OWNER"
        )

class IsTenant(BasePermission):
    def has_permission(self,request,view):
        return(
            request.user,
            request.user.is_authenticated,
            request.user.role=="TENANT"
        )
class IsOwnerOrAdmin(BasePermission):
    def has_permission(self,request,view):
        return(
            request.user,
            request.user.is_authenticated,
            request.user.role in ["OWNER","ADMIN"]
        )
class IsTenantOrAdmin(BasePermission):
    def has_permission(self,request,view):
        return(
            request.user,
            request.user.is_authenticated,
            request.user.role in ["TENANT","ADMIN"]
        )