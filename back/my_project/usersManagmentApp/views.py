from django.shortcuts import render
from django.contrib.auth import get_user_model

User = get_user_model()

from rest_framework.views import APIView , status, Response

from .serializers import (UserSerializer, UserCreateSerializer, SetUserPasswordSerializer,
                          GroupSerializer, PermissionSerializer
                          
                          )



from django.db.models import Q

from usersAuthApp.utils.utils_permissions import  HasUserManagementPermission

from systemSettingsApp.general_utils.custom_utils import IsStaffOrSuperUser




from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType



from usersAuthApp.models import CustomPermission



# all users
class UsersView(APIView):

 
    def get_permissions(self):

        if self.request.method != 'GET':
            # Apply HasUserManagementPermission for all methods except GET
            return [IsStaffOrSuperUser(), HasUserManagementPermission()]
        # For GET, only use IsStaffOrSuperUser (if you wana select a user in dropdown menu inside other app)
        return [IsStaffOrSuperUser()]


    def post(self, request):

        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(is_active=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def get(self, request, id=None):

 
        if id:
            try:
                obj = User.objects.get(id=id)
                serializer =  UserSerializer(obj)
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            except User.DoesNotExist :
                return Response({'message': 'object not found'}, status=status.HTTP_404_NOT_FOUND)

            except Exception as e:
                return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else :

            search_query = request.query_params.get('q', '').strip()
            user_type = request.query_params.get('user_type', 'all')  # 'all', 'staff', 'superuser', 'normal', 'admin'

            queryset = User.objects.all()

            # Filter by user type
            if user_type == 'staff':
                queryset = queryset.filter(is_staff=True)
            elif user_type == 'superuser':
                queryset = queryset.filter(is_superuser=True)
            elif user_type == 'normal':
                queryset = queryset.filter(is_staff=False, is_superuser=False)
            elif user_type == 'admin':
                queryset = queryset.filter(Q(is_staff=True) | Q(is_superuser=True))

            # Apply search filter
            if search_query:
                queryset = queryset.filter(
                    Q(first_name__icontains=search_query) |
                    Q(last_name__icontains=search_query) |
                    Q(email__icontains=search_query)
                )

            serializer = UserSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, id):

        try:
            obj = User.objects.get(id=id)
            serializer =  UserSerializer(obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
        except User.DoesNotExist :
            return Response({'message': 'object not found'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        try:
            obj = User.objects.get(id=id)
            if obj.id == request.user.id:
                return Response( {'message': 'You cannot delete yourself.'}, status=status.HTTP_400_BAD_REQUEST)

            obj.delete()
            return Response({'message' :'object has been deleted'}, status=status.HTTP_202_ACCEPTED)
 
        except User.DoesNotExist :
            return Response({'message': 'object not found'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class SetUserPasswordAPIView(APIView):
	permission_classes = [IsStaffOrSuperUser, HasUserManagementPermission]  

	def post(self, request, id):
		serializer = SetUserPasswordSerializer(data=request.data)
		if not serializer.is_valid():
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		try:
			user = User.objects.get(id=id)
			user.password = make_password(serializer.validated_data['new_password'])
			user.save()
			return Response( {'message': 'Password updated successfully.'}, status=status.HTTP_202_ACCEPTED)
		except User.DoesNotExist:
			return Response({'error': 'User not found.'},status=status.HTTP_404_NOT_FOUND)
		except Exception as e:
			return Response({'error': str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class GroupView(APIView):
    permission_classes = [IsStaffOrSuperUser, HasUserManagementPermission]

    def post(self, request):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, pk=None):
        if pk:
            try:
                group = Group.objects.get(pk=pk)
                serializer = GroupSerializer(group)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Group.DoesNotExist:
                return Response({'error': 'Group not found.'}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e :
                 return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            groups = Group.objects.all()
            serializer = GroupSerializer(groups, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)        
 
    def put(self, request, pk): 
        try:
            group = Group.objects.get(pk=pk)
        except Group.DoesNotExist:
            return Response({'error': 'Group not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e :
                return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serializer = GroupSerializer(group, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            group = Group.objects.get(pk=pk)
            group.delete()
            return Response({'message': 'Group deleted successfully.'}, status=status.HTTP_202_ACCEPTED)
        except Group.DoesNotExist:
            return Response({'error': 'Group not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        




class GetPermissionAPIView(APIView):
 
    def get(self, request, pk=None):
 
        custom_permission_content_type = ContentType.objects.get_for_model(CustomPermission)

        if pk:
            try:
                permission = Permission.objects.filter(content_type=custom_permission_content_type, id=pk).first()
                if permission:
                    serializer = PermissionSerializer(permission)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'Permission not found or not a custom permission.'}, status=status.HTTP_404_NOT_FOUND)
            except Permission.DoesNotExist:
                return Response({'error': 'Permission not found or not a custom permission.'}, status=status.HTTP_404_NOT_FOUND)
        else:
            # List all permissions for the CustomPermission model
            permissions = Permission.objects.filter(content_type=custom_permission_content_type)
            serializer = PermissionSerializer(permissions, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)






 



from django.db import transaction


class GroupAddOrRemovePermissionView(APIView):
    permission_classes = [IsStaffOrSuperUser, HasUserManagementPermission ]  

    @transaction.atomic
    def put(self, request, group_id):
        permission_ids = request.data.get('permissions', [])

        # Validate group existence
        try:
            group = Group.objects.get(id=group_id)
        except Group.DoesNotExist:
            return Response({'message': 'Group not found'}, status=status.HTTP_404_NOT_FOUND)


        custom_permission_content_type = ContentType.objects.get_for_model(CustomPermission)

        # Validate permissions
        permissions = Permission.objects.filter(id__in=permission_ids, content_type=custom_permission_content_type)

        if permissions.count() != len(permission_ids):
            invalid_ids = set(permission_ids) - set(permissions.values_list('id', flat=True))
            return Response({'message': f'Invalid permission IDs: {list(invalid_ids)}'}, status=status.HTTP_400_BAD_REQUEST)

        # Assign permissions (replace all)
        group.permissions.set(permissions)

        # Serialize and return updated permissions
        serializer = PermissionSerializer(permissions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    




class UserPermissionView(APIView):
    permission_classes = [IsStaffOrSuperUser, HasUserManagementPermission]


    def get(self, request, id):
        try:
            user = User.objects.get(id=id)
            permissions = user.user_permissions.all()
            serializer = PermissionSerializer(permissions, many=True)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




    @transaction.atomic
    def put(self, request, id):
        permission_ids = request.data.get('permissions', [])

        # Validate user existence
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        # Filter only permissions related to CustomPermission model
        custom_permission_content_type = ContentType.objects.get_for_model(CustomPermission)
        permissions = Permission.objects.filter(id__in=permission_ids, content_type=custom_permission_content_type)

        # Validate permission IDs
        if permissions.count() != len(permission_ids):
            valid_ids = set(permissions.values_list('id', flat=True))
            invalid_ids = set(permission_ids) - valid_ids
            return Response({'message': f'Invalid permission IDs: {list(invalid_ids)}'}, status=status.HTTP_400_BAD_REQUEST)

        # Assign (replace all) permissions to the user
        user.user_permissions.set(permissions)

        # Serialize and return updated permissions
        serializer = PermissionSerializer(permissions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    


class UserGroupView(APIView):
    permission_classes = [IsStaffOrSuperUser, HasUserManagementPermission]

    def get(self, request, id):
        try:
            user = User.objects.get(id=id)
            groups = user.groups.all()
            serializer = GroupSerializer(groups, many=True)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @transaction.atomic
    def put(self, request, id):
        group_ids = request.data.get('groups', [])

        # Validate user existence
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        # Validate groups
        groups = Group.objects.filter(id__in=group_ids)

        if groups.count() != len(group_ids):
            valid_ids = set(groups.values_list('id', flat=True))
            invalid_ids = set(group_ids) - valid_ids
            return Response({'message': f'Invalid group IDs: {list(invalid_ids)}'}, status=status.HTTP_400_BAD_REQUEST)

        # Assign (replace all) groups to the user
        user.groups.set(groups)

        # Serialize and return updated groups
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)