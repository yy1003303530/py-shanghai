from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
# Create your views here.


class PageViewList(APIView):
    permission_classes = ()
    def get(self,request,format=None):
        queryset = Page.objects.all()
        s = PageSerializers(queryset,many=True)
        return  Response(s.data)
    def post(self,request,format=None):
        s = PageSerializers(data=request.data)
        if s.is_valid():
            s.save()
            return  Response(s.data,status=status.HTTP_201_CREATED)
        return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)
def index(request):
    return HttpResponse('INDEX')


