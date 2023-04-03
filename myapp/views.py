from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from .models import Mmodal
from .serializers import EmpSerializer
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def Home(request):
    return Response("API calling")
@api_view(['GET'])
def emplist(request):
    emp=Mmodal.objects.all()
    serializer=EmpSerializer(emp,many=True)
    return Response(serializer.data)
@api_view(['POST'])
def add_items(request):
    item = EmpSerializer(data=request.data)
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def delete_items(request, pk):
    item = get_object_or_404(Mmodal, pk=pk)
    item.delete()
    return Response("Deleted")
@api_view(['PUT'])
def update_items(request, pk):
    item = Mmodal.objects.get(pk=pk)
    serializer = EmpSerializer(item, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response("error")



def my_api_view(request):

    data = list(Mmodal.objects.all().values())
    return JsonResponse(data, safe=False)