




from rest_framework.views import APIView , Response, status

from ..models import (RequestService, RequestAgent,
                    RequestServicePrivateNote, RequestAgentPrivateNote,
                    SpeedPackagePrice,TrafficPackagePrice, UnlimitedSpeedTrafficPackagePrice
                    )


from ..serializers_package.staff_serializers import (RequestServiceSerializer, RequestAgentSerializer, RequestServicePrivateNoteSerializer,
                                                     RequestAgentPrivateNoteSerializer,SpeedPackagePriceSerializer,TrafficPackagePriceSerializer, UnlimitedSpeedTrafficPackagePriceSerializer  
                                                    
                                                     )


from django.shortcuts import get_object_or_404 

from ..utils import get_client_ip, IsStaffOrSuperUser, MyCustomPagination

from rest_framework.permissions import AllowAny
from django.db.models import Q



class UnlimitedSpeedTrafficPackagePriceView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):

        serializer = UnlimitedSpeedTrafficPackagePriceSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()  
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


    def get(self, request, id=None):
        if id:
            try:
                obj = UnlimitedSpeedTrafficPackagePrice.objects.get(id=id)
                serializer = UnlimitedSpeedTrafficPackagePriceSerializer(obj)
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            except UnlimitedSpeedTrafficPackagePrice.DoesNotExist:
                return Response({'message' : "object not found"}, status=status.HTTP_404_NOT_FOUND)

            except Exception as e :
                return Response({'message' : str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else :
            obj_list = UnlimitedSpeedTrafficPackagePrice.objects.all()
            serializer = UnlimitedSpeedTrafficPackagePriceSerializer(obj_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, id):
        obj = get_object_or_404(UnlimitedSpeedTrafficPackagePrice, id=id)

        serializer = UnlimitedSpeedTrafficPackagePriceSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        obj = get_object_or_404(UnlimitedSpeedTrafficPackagePrice, id=id)
        try:
            obj.delete()
            return Response({'message' : 'object has been deleted'}, status=status.HTTP_202_ACCEPTED)
         
        except Exception as e :
            return Response({'message' : str(e)}, status=status.HTTP_400_BAD_REQUEST)







class TrafficPackagePriceView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):

        serializer = TrafficPackagePriceSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()  
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


    def get(self, request, id=None):
        if id:
            try:
                obj = TrafficPackagePrice.objects.get(id=id)
                serializer = TrafficPackagePriceSerializer(obj)
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            except TrafficPackagePrice.DoesNotExist:
                return Response({'message' : "object not found"}, status=status.HTTP_404_NOT_FOUND)

            except Exception as e :
                return Response({'message' : str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else :
            obj_list = TrafficPackagePrice.objects.all()
            serializer = TrafficPackagePriceSerializer(obj_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, id):
        obj = get_object_or_404(TrafficPackagePrice, id=id)

        serializer = TrafficPackagePriceSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        obj = get_object_or_404(TrafficPackagePrice, id=id)
        try:
            obj.delete()
            return Response({'message' : 'object has been deleted'}, status=status.HTTP_202_ACCEPTED)
         
        except Exception as e :
            return Response({'message' : str(e)}, status=status.HTTP_400_BAD_REQUEST)






class SpeedPackagePriceView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):

        serializer = SpeedPackagePriceSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()  
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


    def get(self, request, id=None):
        if id:
            try:
                obj = SpeedPackagePrice.objects.get(id=id)
                serializer = SpeedPackagePriceSerializer(obj)
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            except SpeedPackagePrice.DoesNotExist:
                return Response({'message' : "object not found"}, status=status.HTTP_404_NOT_FOUND)

            except Exception as e :
                return Response({'message' : str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else :
            obj_list = SpeedPackagePrice.objects.all()
            serializer = SpeedPackagePriceSerializer(obj_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, id):
        obj = get_object_or_404(SpeedPackagePrice, id=id)

        serializer = SpeedPackagePriceSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        obj = get_object_or_404(SpeedPackagePrice, id=id)
        try:
            obj.delete()
            return Response({'message' : 'object has been deleted'}, status=status.HTTP_202_ACCEPTED)
         
        except Exception as e :
            return Response({'message' : str(e)}, status=status.HTTP_400_BAD_REQUEST)





class RequestAgentPrivateNoteView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, request_id):

        data = request.data.copy()
        data['request_agent'] = request_id
        serializer = RequestAgentPrivateNoteSerializer(data=data)
        if serializer.is_valid():
            user = request.user if request.user.is_authenticated else None

            serializer.save(created_ip_address=get_client_ip(request), user=user)  # set it here

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


    def get(self, request, request_id,  id=None):
        if id:
            try:
                obj = RequestAgentPrivateNote.objects.get(id=id)
                serializer = RequestAgentPrivateNoteSerializer(obj)
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            except RequestAgentPrivateNote.DoesNotExist:
                return Response({'message' : "object not found"}, status=status.HTTP_404_NOT_FOUND)

            except Exception as e :
                return Response({'message' : str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else :

            obj_list = RequestAgentPrivateNote.objects.filter(request_agent=request_id)
            serializer = RequestAgentPrivateNoteSerializer(obj_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request,request_id, id):
        obj = get_object_or_404(RequestAgentPrivateNote, id=id)

        serializer = RequestAgentPrivateNoteSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,request_id, id):
        obj = get_object_or_404(RequestAgentPrivateNote, id=id)
        try:
            obj.delete()
            return Response({'message' : 'object has been deleted'}, status=status.HTTP_202_ACCEPTED)
         
        except Exception as e :
            return Response({'message' : str(e)}, status=status.HTTP_400_BAD_REQUEST)






class RequestServicePrivateNoteView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, request_id):

        data = request.data.copy()
        data['request_service'] = request_id
        serializer = RequestServicePrivateNoteSerializer(data=data)
        if serializer.is_valid():
            user = request.user if request.user.is_authenticated else None

            serializer.save(created_ip_address=get_client_ip(request), user=user)  # set it here

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


    def get(self, request, request_id,  id=None):
        if id:
            try:
                obj = RequestServicePrivateNote.objects.get(id=id)
                serializer = RequestServicePrivateNoteSerializer(obj)
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            except RequestServicePrivateNote.DoesNotExist:
                return Response({'message' : "object not found"}, status=status.HTTP_404_NOT_FOUND)

            except Exception as e :
                return Response({'message' : str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else :

            obj_list = RequestServicePrivateNote.objects.filter(request_service=request_id)
            serializer = RequestServicePrivateNoteSerializer(obj_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request,request_id, id):
        obj = get_object_or_404(RequestServicePrivateNote, id=id)

        serializer = RequestServicePrivateNoteSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,request_id, id):
        obj = get_object_or_404(RequestServicePrivateNote, id=id)
        try:
            obj.delete()
            return Response({'message' : 'object has been deleted'}, status=status.HTTP_202_ACCEPTED)
         
        except Exception as e :
            return Response({'message' : str(e)}, status=status.HTTP_400_BAD_REQUEST)










class RequestAgentView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):

        serializer = RequestAgentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_ip_address=get_client_ip(request))  # set it here

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


    def get(self, request, id=None):
        if id:
            try:
                obj = RequestAgent.objects.get(id=id)
                serializer = RequestAgentSerializer(obj)
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            except RequestAgent.DoesNotExist:
                return Response({'message' : "object not found"}, status=status.HTTP_404_NOT_FOUND)

            except Exception as e :
                return Response({'message' : str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else :
            phone_number = request.query_params.get('phone_number', None)

            if phone_number:
                obj_list = RequestAgent.objects.filter(Q(phone_number__icontains=phone_number))
            else:
                obj_list = RequestAgent.objects.all()

            paginator = MyCustomPagination()
            page = paginator.paginate_queryset(obj_list, request)
            serializer = RequestAgentSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data) 


    def put(self, request, id):
        obj = get_object_or_404(RequestAgent, id=id)
        serializer = RequestAgentSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        obj = get_object_or_404(RequestAgent, id=id)
        try:
            obj.delete()
            return Response({'message' : 'object has been deleted'}, status=status.HTTP_202_ACCEPTED)
         
        except Exception as e :
            return Response({'message' : str(e)}, status=status.HTTP_400_BAD_REQUEST)






class RequestServiceView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):

        serializer = RequestServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_ip_address=get_client_ip(request))  # set it here

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, id=None):
        if id:
            try:
                obj = RequestService.objects.get(id=id)
                serializer = RequestServiceSerializer(obj)
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            except RequestService.DoesNotExist:
                return Response({'message' : "object not found"}, status=status.HTTP_404_NOT_FOUND)

            except Exception as e :
                return Response({'message' : str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else :
            phone_number = request.query_params.get('phone_number', None)


            if phone_number:
                obj_list = RequestService.objects.filter(Q(phone_number__icontains=phone_number))
            else:
                obj_list = RequestService.objects.all()


            paginator = MyCustomPagination()
            page = paginator.paginate_queryset(obj_list, request)
            serializer = RequestServiceSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data) 


    def put(self, request, id):
        obj = get_object_or_404(RequestService, id=id)
        serializer = RequestServiceSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        obj = get_object_or_404(RequestService, id=id)
        try:
            obj.delete()
            return Response({'message' : 'object has been deleted'}, status=status.HTTP_202_ACCEPTED)
         
        except Exception as e :
            return Response({'message' : str(e)}, status=status.HTTP_400_BAD_REQUEST)