from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
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

	def me(self, request, *args, **kwargs):
		self.object = get_object_or_404(myModels.User, pk=request.user.id)
		serializer = self.get_serializer(self.object)
		return Response(serializer.data)

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