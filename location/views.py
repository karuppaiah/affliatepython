from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from location.models import Location
from location.serializers import LocationSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
#class JSONResponse(HttpResponse):
#    """
#    #An HttpResponse that renders its content into JSON
#    """
#    def __init__(self, data, **kwargs):
#        content = JSONRenderer().render(data)
#        kwargs['content_type']= 'application/json'
#        super(JSONResponse,self).__init__(content, **kwargs)
 







#@csrf_exempt
@api_view(['GET','POST'])
def location_list(request,format=None):
    """ 
    list all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many = True)
        return Response(serializer.data)
    elif request/method == 'POST':
        serializer = LocationSerializer(request.data)
        if serializers.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.error, status =status.HTTP_400_BAD_REQUEST) 

#@csrf_exempt
@api_view(['PUT','GET','DELETE'])
def location_detail(request, pk,format=None):
    """
    Retrieve, update or delete a code location.
    """
    try:
        location = Location.objects.get(pk=pk)
    except Location.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LocationSerializer(location)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LocationSerializer(location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        location.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
# Create your views here.
       
