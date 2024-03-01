from operator import contains
from token import EQUAL
from uuid import UUID
from rest_framework import permissions

from src.users.models import Analysis, User


class IsUserOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        if obj == request.user or request.user.is_superuser:
            return True

class IFUserisAnalyst(permissions.BasePermission): 
    def has_object_permission(self, request, view, obj): 

        # user = User.objects.get(id = request.user.id)
        # user_analysts = user.subscribe_analysts.all()
        # for sub_id in user_analysts:
        #     if UUID(sub_id) == obj.id:
        #         sub_id = obj.id
        
        # if request.method in permissions.SAFE_METHODS:
        #     if obj.id == UUID(sub_id): 
        #         return True
        
        if obj.analyst_user_id == request.user.id:
            return True
        
        return False
    

class Createanalysis(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.user.is_analyst is True:
            return True
        
            
