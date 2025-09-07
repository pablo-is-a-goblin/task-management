from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from . import serializers
from rest_framework import viewsets
from . import models as myModels
from django.shortcuts import get_object_or_404

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
			'unit_url' : self.unit_url,
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