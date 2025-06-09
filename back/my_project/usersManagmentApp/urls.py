
from django.urls import path

from .views import (UsersView, SetUserPasswordAPIView, GroupView, GetPermissionAPIView,
                    GroupAddOrRemovePermissionView, UserPermissionView, UserGroupView
                    
                    )






urlpatterns = [

    path('staff/users/', UsersView.as_view()),
    path('staff/users/<int:id>/', UsersView.as_view()),
    path('staff/users/<int:id>/set_password/', SetUserPasswordAPIView.as_view()),
    path('staff/users/<int:id>/permission/', UserPermissionView.as_view(), name='assign-remove-permission'),
    path('staff/users/<int:id>/group/', UserGroupView.as_view(), name='assign-remove-group'),
 

    path('staff/group/', GroupView.as_view()), # add / remove / edit / list  / groups 
    path('staff/group/<int:pk>/', GroupView.as_view()), # get object or put or delete group
    path('staff/group/<int:group_id>/permissions/', GroupAddOrRemovePermissionView.as_view()), # add or remove permissions to a group in post request


    path('staff/get_permissions/', GetPermissionAPIView.as_view()), # get list   permission
    path('staff/get_permissions/<int:pk>/', GetPermissionAPIView.as_view()), # get  obj permission



]