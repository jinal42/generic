from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics


from .models import Custom
from .serializers import CustomSerializer

from rest_framework import viewsets
from rest_framework import status

from rest_framework.authentication import BasicAuthentication,SessionAuthentication
# from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly

from .custompermissions import MyPermission



# Class based view to Get User Details using Token Authentication

class StudDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  
  def get(self,request,*args,**kwargs):
    user = Custom.objects.get(id=request.user.id)
    serializer = CustomSerializer(user)
      
    return Response(serializer.data)

  


# Model ViewSet
class CustomModelViewSet(viewsets.ModelViewSet):
   queryset=Custom.objects.all()
   serializer_class=CustomSerializer

   authentication_classes=[SessionAuthentication]
   permission_classes=[MyPermission]
#    permission_classes=[IsAdminUser]
#    permission_classes=[AllowAny]
#    permission_classes=[IsAuthenticatedOrReadOnly]
#    permission_classes=[DjangoModelPermissions]
   # permission_classes=[DjangoModelPermissionsOrAnonReadOnly]

