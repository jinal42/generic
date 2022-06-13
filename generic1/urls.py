from django.urls import path
from .views import StudListCreate, UserDetailAPI,RegisterUserAPIView
from .views import CustomList,CustomCreate,CustomRetrive,CustomDestory,CustomUpdate


from .views import StudList,StudCreate,StudRetrive,StudUpdate,StudDelete
from .views import StudList,StudRU,StudRD,StudRUD


urlpatterns = [
  path("get-details",UserDetailAPI.as_view()),
  path('reg',RegisterUserAPIView.as_view()),

  path('list',CustomList.as_view()),
  path('create',CustomCreate.as_view()),
  path('retrive/<int:pk>',CustomRetrive.as_view()),
  path('update/<int:pk>',CustomUpdate.as_view()), 
  path('delete/<int:pk>',CustomDestory.as_view()),


  path('ConList',StudList.as_view()),
  path('ConCreate',StudCreate.as_view()),
  path('ConRetrive/<int:pk>',StudRetrive.as_view()),
  path('ConUpdate/<int:pk>',StudUpdate.as_view()),
  path('ConDelete/<int:pk>',StudDelete.as_view()),


  path('ConListCreate',StudListCreate.as_view()),
  path('ConRU/<int:pk>',StudRU.as_view()),
  path('ConRD/<int:pk>',StudRD.as_view()),
  path('ConRUD/<int:pk>',StudRUD.as_view()),




]
