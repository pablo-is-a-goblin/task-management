from django.urls import path
from . import views

app_name="tasks"
urlpatterns = [
    path('', views.TasksViewSet.as_view({'get': 'list', 'post': 'create'}), name="list"),
    path('<int:pk>', views.TasksViewSet.as_view({'get': 'retrieve',
                                                      'post': 'update'}), name="unit"),
]