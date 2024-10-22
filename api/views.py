from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from notesmain.models import Notes
from .serializers import NotesSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@api_view(['GET'])
def getData(request, format=None):
    note = Notes.objects.all()
    serializer = NotesSerializer(note, many= True)
    return Response(serializer.data)


@api_view(['POST'])
def addData(request, format=None):
    serializer = NotesSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['GET','PUT', 'DELETE'])
def detailData(request, id, format=None):
    note = Notes.objects.get(pk=id)

    if request.method == 'GET':
        serializer= NotesSerializer(note)
        return Response(serializer.data)
    

    elif request.method == 'PUT':
        serializer = NotesSerializer(data= request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        else:
            return Response(serializer.errors, status= status.HTTP_403_FORBIDDEN)

    elif request.method == 'DELETE':
        note.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    