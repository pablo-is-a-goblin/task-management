from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from . import serializers
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework import viewsets
from . import models as myModels
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import AllowAny

# Create your views here.
class  ProfilesViewSet(viewsets.ModelViewSet):
	queryset = myModels.User.objects.all()
	serializer_class = serializers.UserSerializer
	renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
	template_name='profile.html'

	def me(self, request, *args, **kwargs):
		return self.retrieve(request, request.user.id)
	
	def retrieve(self, request, pk):
		self.object = get_object_or_404(myModels.User, pk=pk)
		return Response({'serializer': self.get_serializer(self.object), 'profile': self.object})
	
	def list(self, request):
		return Response({
			'queryset' : self.queryset, 
			'type': 'Profiles',
			'unit_url' : 'users:user'}, template_name='list.html')
	
	def update(self, request, pk):
		super().update(request, pk)
		return self.retrieve(request, pk)

class	UserRegisterAPIView(APIView):
	permission_classes = [AllowAny]
	
	def sing_up_succesfull_response(self, serializer):
		response = {
			'success': True,
			'user': serializer.data,
		}
		return (response)

	def post(self, request):
		serializer = serializers.RegisterSerializer(data=request.data)
		if (serializer.is_valid()):
			serializer.save()
			response = self.sing_up_succesfull_response(serializer)
			login(request, authenticate(username=request.data["username"], password=request.data["password"]))
			return redirect("profile")
		raise ValidationError(serializer.errors, code=status.HTTP_406_NOT_ACCEPTABLE)