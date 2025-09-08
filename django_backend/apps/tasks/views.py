from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from . import serializers
from rest_framework import viewsets
from . import models as myModels
from django.shortcuts import get_object_or_404
from apps.tasks.tasks import send_task_notification

# Create your views here.
class  TasksViewSet(viewsets.ModelViewSet):
	queryset = myModels.Task.objects.all()
	serializer_class = serializers.TaskSerializer
	renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
	template_name='unit.html'
	type_name = 'Tasks'
	unit_url = 'tasks:unit'
	list_url = 'tasks:list'

	def create(self, request):
		super().create(request)
		self.queryset = myModels.Task.objects.all()
		return self.list(request)

	def retrieve(self, request, pk):
		self.object = get_object_or_404(myModels.Task, pk=pk)
		return Response({
			'serializer': self.get_serializer(self.object), 
			'unit': self.object,
			'unit_url' : self.unit_url,
			'list_url' : self.list_url,
			'type': self.type_name,
			})
	
	def list(self, request):
		return Response({
			'queryset' : myModels.Task.objects.all(), 
			'type': self.type_name,
			'unit_url' : self.unit_url,
			'list_url' : self.list_url,
			'serializer': self.get_serializer()}, template_name='list.html')
	
	def update(self, request, pk):
		super().update(request, pk)
		return self.retrieve(request, pk)
	
	def assign_list(self, request, pk):
		self.object = get_object_or_404(myModels.Task, pk=pk)
		return Response({
			'serializer': serializers.TaskAssignment(self.object), 
			'unit': self.object,
			'unit_url' : 'tasks:assign',
			'type' : "Assignment List"
			})
	
	def update_assign(self, request, pk):
		self.serializer_class = serializers.TaskAssignment
		self.update(request, pk)
		send_task_notification.delay(pk, 'assignment')
		return self.assign_list(request, pk)


class  TagsViewSet(viewsets.ModelViewSet):
	queryset = myModels.Tag.objects.all()
	serializer_class = serializers.TagSerializer
	renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
	template_name='unit.html'
	type_name = 'Tags'
	unit_url = 'tags:unit'
	list_url = 'tags:list'

	def create(self, request):
		super().create(request)
		self.queryset = myModels.Tag.objects.all()
		return self.list(request)

	def retrieve(self, request, pk):
		self.object = get_object_or_404(myModels.Tag, pk=pk)
		return Response({
			'serializer': self.get_serializer(self.object), 
			'unit': self.object,
			'list_url' : self.list_url,
			'unit_url' : self.unit_url,
			'type' : self.type_name
			})
	
	def list(self, request):
		return Response({
			'queryset' : self.queryset, 
			'type': self.type_name,
			'unit_url' : self.unit_url,
			'list_url' : self.list_url,
			'serializer': self.get_serializer()}, template_name='list.html')
	
	def update(self, request, pk):
		super().update(request, pk)
		return self.retrieve(request, pk)