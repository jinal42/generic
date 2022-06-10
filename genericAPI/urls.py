


from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken import views


from rest_framework.routers import DefaultRouter
from generic1 import  views as v

router = DefaultRouter()
router.register('viewsett',v.StudViewSet,basename='cust')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('generic1.urls')),
    path('api-token-auth', views.obtain_auth_token),
    path('',include(router.urls)),

]
