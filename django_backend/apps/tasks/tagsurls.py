from django.urls import path
from . import views

app_name="tags"
urlpatterns = [
    path('', views.TagsViewSet.as_view({'get': 'list', 
                                        'post': 'create',}), name="list"),
    path('<int:pk>', views.TagsViewSet.as_view({'get': 'retrieve',
                                                'post': 'update',
                                                'delete': 'destroy'}), name="unit"),
]