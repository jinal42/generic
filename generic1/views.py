from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics


from .models import CustomUser
from .serializers import TodoSerializer
from rest_framework import status


from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin


from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView

from rest_framework import viewsets
from rest_framework import status

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser

# Class based view to Get User Details using Token Authentication

class UserDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  
  def get(self,request,*args,**kwargs):
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
      
    return Response(serializer.data)

  def get(self, request, *args, **kwargs):
        ''' List all the todo items for given requested user '''
        todos = CustomUser.objects.filter(user = request.user.id)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
  def post(self, request, *args, **kwargs):
        ''' Create the Todo with given todo data '''
        data = {
            'phone': request.data.get('phone'), 
            'user': request.user.id
        }
        serializer = TodoSerializer(data=data)
        print("🚀 ~ file: views.py ~ line 48 ~ serializer", serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):  
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer




class CustomList(GenericAPIView,ListModelMixin):
  queryset=User.objects.all()
  serializer_class=UserSerializer
  print("🚀 ~ file: views.py ~ line 69 ~ queryset", queryset)

  def get(self,request,*args,**kwrgs):
    print('_______________________________________________')
    return self.list(request,*args,**kwrgs)

class CustomCreate(GenericAPIView,CreateModelMixin):
  queryset=User.objects.all()
  serializer_class=UserSerializer

  def post(self,request,*args,**kwrgs):
    return self.create(request,*args,**kwrgs)
 
class CustomRetrive(GenericAPIView,RetrieveModelMixin):
  queryset=User.objects.all()
  serializer_class=UserSerializer

  def get(self,request,*args,**kwrgs):
    return self.retrieve(request,*args,**kwrgs)
 

class CustomDestory(GenericAPIView,DestroyModelMixin):
  queryset=User.objects.all()
  serializer_class=UserSerializer

  def delete(self,request,*args,**kwrgs):
    return self.destroy(request,*args,**kwrgs)
 
class CustomUpdate(GenericAPIView,UpdateModelMixin):
  queryset=User.objects.all()
  serializer_class=UserSerializer

  def post(self,request,*args,**kwrgs):
    return self.update(request,*args,**kwrgs)
 




 # Concrete View Classes
class StudList(ListAPIView):
   queryset=User.objects.all()
   serializer_class=UserSerializer

class StudCreate(CreateAPIView):
   queryset=User.objects.all()
   serializer_class=UserSerializer

class StudRetrive(RetrieveAPIView):
   queryset=User.objects.all()
   serializer_class=UserSerializer

class StudUpdate(UpdateAPIView):
   queryset=User.objects.all()
   serializer_class=UserSerializer

   
class StudDelete(DestroyAPIView):
   queryset=User.objects.all()
   serializer_class=UserSerializer


# Combine Concrete View Classes

class StudListCreate(ListCreateAPIView):
   queryset=User.objects.all()
   serializer_class=UserSerializer

class StudRU(RetrieveUpdateAPIView):
   queryset=User.objects.all()
   serializer_class=UserSerializer


class StudRD(RetrieveDestroyAPIView):
   queryset=User.objects.all()
   serializer_class=UserSerializer

class StudRUD(RetrieveUpdateDestroyAPIView):
   queryset=User.objects.all()
   serializer_class=UserSerializer


#ViewSets
class StudViewSet(viewsets.ViewSet):
  def list(self,req):
   queryset=User.objects.all()
   serializers=UserSerializer(queryset,many=True)
   return Response(serializers.data)

# Model ViewSet
class StudModelViewSet(viewsets.ModelViewSet):
   queryset=User.objects.all()
   serializer_class=UserSerializer

#ReadOnly Model ViewSet 
class StudReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
   queryset=User.objects.all()
   serializer_class=UserSerializer

class Cust(viewsets.ModelViewSet):
   queryset=CustomUser.objects.all()
   serializer_class=TodoSerializer
   authentication_classes=[BasicAuthentication]
   # permission_classes=[IsAuthenticated]
   permission_classes=[IsAdminUser]


class Cust1(viewsets.ModelViewSet):
   queryset=CustomUser.objects.all()
   serializer_class=TodoSerializer
   authentication_classes=[BasicAuthentication]
   # permission_classes=[IsAuthenticated]
   permission_classes=[AllowAny]