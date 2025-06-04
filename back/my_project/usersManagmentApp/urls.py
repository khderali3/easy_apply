
from django.urls import path

from .views import UsersView, SetUserPasswordAPIView, GroupView, GetPermissionAPIView, GroupAddOrRemovePermissionView 






urlpatterns = [

    path('users/', UsersView.as_view()),
    path('users/<int:id>/', UsersView.as_view()),
    path('users/<int:id>/set_password/', SetUserPasswordAPIView.as_view()),


    path('group/', GroupView.as_view()), # add / remove / edit / list  / groups 
    path('group/<int:pk>/', GroupView.as_view()), # get object or put or delete group
    path('group/<int:group_id>/permissions/', GroupAddOrRemovePermissionView.as_view()), # add or remove permissions to a group in post request







    path('get_permissions/', GetPermissionAPIView.as_view()), # get list   permission
    path('get_permissions/<int:pk>/', GetPermissionAPIView.as_view()), # get  obj permission



]