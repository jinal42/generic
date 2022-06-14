from django.contrib import admin
from django.urls import path,include
# from rest_framework.authtoken import views


from rest_framework.routers import DefaultRouter
from generic1 import  views as v

router = DefaultRouter()

router.register('viewsett',v.StudViewSet,basename='ViewSett')                   
router.register('modelviewsett',v.StudModelViewSet,basename='ModelViewSett')
router.register('readOnlyModelViewsett',v.StudReadOnlyModelViewSet,basename='Read_only')

router.register('cust',v.Cust,basename='cust')
router.register('cust1',v.Cust1,basename='cust1')


from session import  views as vSession

# session app:
router.register('session',vSession.StudendModelViewSet,basename='s1')




from customPer import  views as vCustom

# customPer app:
router.register('customPer',vCustom.CustomModelViewSet,basename='c1')




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('generic1.urls')),
    # path('api-token-auth', views.obtain_auth_token),
    path('',include(router.urls)),
    # path('list',vSession.StudendModelViewSet.as_view()),
    path('auth/',include('rest_framework.urls')),

]
