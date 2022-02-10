from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from authentication.serializers import AssociatesMasterSerializer
from authentication.models import AssociatesMasterModel

class AssociateMasterAPIView(APIView):
    #for getting data by id , by serach associate name and all data
    def get(self,request,*args,**kwargs):
        request_data = request.GET
        output_data, output_status = [], False
        res_status = status.HTTP_400_BAD_REQUEST
        # if we are getting id 
        if request_data.get("id",False):
            ass_obj = AssociatesMasterModel.objects.filter(pk = id).first()
        # if we are getting search parameter
        elif request_data.get("search",False):
            ass_obj = AssociatesMasterModel.objects.filter(name__icontains = request_data['search']).first()
        # all data
        else:
            ass_obj = AssociatesMasterModel.objects.all()
        if ass_obj:
            serializer = AssociatesMasterSerializer(ass_obj,many=True)
            output_data, output_status = serializer.data, True
            res_status = status.HTTP_200_OK
        context = {
            "data":output_data,
            "status":output_status
        }
        return Response(context,status = res_status,content_type="application/json")
    
    def update(request,instance):
        serializer = AssociatesMasterSerializer(instance,data = request.data)
        if serializer.is_valid():
            serializer.save()
            output_data = "Updated"
        else:
            output_data = serializer.errors
        context = {
            "data":output_data
        }
        return Response(context,content_type="application/json")
   
    def post(self,request,*args,**kwargs):
        output_data, output_status = [], False
        res_status = status.HTTP_400_BAD_REQUEST
        # if we want to update by id 
        if request.GET.get("id",False):
            instance = AssociatesMasterModel.obejcts.filter(pk = id).first()
            if instance:
                return self.update(request, instance)
        # if new data we want to add
        serializer = AssociatesMasterSerializer(data = request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            output_data, output_status = "Success", True
            res_status = status.HTTP_200_OK
        else:
            output_data = serializer.errors
        context = {
            "data":output_data,
            "status":output_status
        }
        return Response(context,status = res_status,content_type="application/json")
        
    def delete(self,request):
        # for deleting obj
        output_data, output_status = [], False
        res_status = status.HTTP_400_BAD_REQUEST
        instance = AssociatesMasterModel.objects.filter(pk = request.GET.get("id")).first()
        if instance:
            instance.delete()
            output_data, output_status = "Deleted", True
            res_status = status.HTTP_200_OK
        context = {
            "data":output_data,
            "status":output_status
        }
        return Response(context,status = res_status,content_type="application/json")
        
        



        

                 
        