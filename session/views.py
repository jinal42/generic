from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics


from .models import Student
from .serializers import StudentSerializer

from rest_framework import viewsets
from rest_framework import status

from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly



# Class based view to Get User Details using Token Authentication

class StudDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  
  def get(self,request,*args,**kwargs):
    user = Student.objects.get(id=request.user.id)
    serializer = StudentSerializer(user)
      
    return Response(serializer.data)

  


# Model ViewSet
class StudendModelViewSet(viewsets.ModelViewSet):
   queryset=Student.objects.all()
   serializer_class=StudentSerializer

   authentication_classes=[SessionAuthentication]
#    permission_classes=[IsAuthenticated]
#    permission_classes=[IsAdminUser]
#    permission_classes=[AllowAny]
#    permission_classes=[IsAuthenticatedOrReadOnly]
#    permission_classes=[DjangoModelPermissions]
   permission_classes=[DjangoModelPermissionsOrAnonReadOnly]

