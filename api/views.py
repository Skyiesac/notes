from rest_framework.response import Response
from rest_framework import status , generics
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny , IsAuthenticated
from notesmain.models import Notes
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User
from .serializers import NotesSerializer , UserSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
# Create your views here.


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'username': user.username}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProtectedView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message': 'This is a protected view!'})

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
    