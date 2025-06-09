from django.shortcuts import render

# Create your views here.

from .serializer import MainConfigurationSerializer, QueuedEmailSerializer
from .models import MainConfiguration, QueuedEmail
from rest_framework.views import APIView , status, Response

from .general_utils.custom_utils import IsStaffOrSuperUser



class MainConfigurationView(APIView):

    permission_classes = [IsStaffOrSuperUser]

    def get(self, request):
        obj = MainConfiguration.get_solo()
        serializer = MainConfigurationSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request):
        obj = MainConfiguration.get_solo()
        serializer = MainConfigurationSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



class QueuedEmailView(APIView):
    permission_classes = [IsStaffOrSuperUser]

    def get(self, request):
        obj_list = QueuedEmail.objects.all()
        serializer = QueuedEmailSerializer(obj_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request):
 

        # permission_ids = request.data.get('permissions', [])

        # # Validate user existence
        # try:
        #     user = User.objects.get(id=id)
        # except User.DoesNotExist:
        #     return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        # # Filter only permissions related to CustomPermission model
        # custom_permission_content_type = ContentType.objects.get_for_model(CustomPermission)
        # permissions = Permission.objects.filter(id__in=permission_ids, content_type=custom_permission_content_type)

        # # Validate permission IDs
        # if permissions.count() != len(permission_ids):
        #     valid_ids = set(permissions.values_list('id', flat=True))
        #     invalid_ids = set(permission_ids) - valid_ids
        #     return Response({'message': f'Invalid permission IDs: {list(invalid_ids)}'}, status=status.HTTP_400_BAD_REQUEST)








        try:
            ids = request.data.get('ids', [])



            if not isinstance(ids, list) or not all(isinstance(i, int) for i in ids):
                return Response({"detail": "Invalid 'ids' format. Must be a list of integers."}, status=status.HTTP_400_BAD_REQUEST)

            valied_objects = QueuedEmail.objects.filter(id__in=ids)
            if valied_objects.count() != len(ids):
                valid_ids = set(valied_objects.values_list('id', flat=True))
                invalid_ids = set(ids) - valid_ids
                return Response({'message': f'Invalid values: {list(invalid_ids)}'}, status=status.HTTP_400_BAD_REQUEST)



            deleted_count, _ = QueuedEmail.objects.filter(id__in=ids).delete()
            return Response({"deleted_count": deleted_count}, status=status.HTTP_202_ACCEPTED)


        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




        # try:
        #     ids = request.data.get('ids', [])



        #     if not isinstance(ids, list) or not all(isinstance(i, int) for i in ids):
        #         return Response({"detail": "Invalid 'ids' format. Must be a list of integers."}, status=status.HTTP_400_BAD_REQUEST)


        #     deleted_count, _ = QueuedEmail.objects.filter(id__in=ids).delete()
        #     return Response({"deleted_count": deleted_count}, status=status.HTTP_202_ACCEPTED)


        # except Exception as e:
        #     return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 


class QueuedEmailDeleteAllView(APIView):
        
    permission_classes = [IsStaffOrSuperUser]

    def delete(self, request):
  
        try:
            deleted_count, _ = QueuedEmail.objects.all().delete()
            return Response({"deleted_count": deleted_count}, status=status.HTTP_202_ACCEPTED)

        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




