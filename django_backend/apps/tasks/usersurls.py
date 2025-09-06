from django.urls import path, include
from . import views
from rest_framework import permissions
from rest_framework import authentication

urlpatterns = [
    path('', views.ProfilesViewSet.as_view({'get': 'list'})),
    path('<int:pk>', views.ProfilesViewSet.as_view({'get': 'retrieve',
                                                      'put': 'update'})),
    path('me', views.ProfilesViewSet.as_view({'get': 'me'},
        permission_classes = [permissions.IsAuthenticated], 
		authentication_classes = [authentication.SessionAuthentication],))

]