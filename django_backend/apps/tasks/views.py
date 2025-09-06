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

# Create your views here.
class  ProfilesViewSet(viewsets.ModelViewSet):
	queryset = myModels.User.objects.all()
	serializer_class = serializers.UserSerializer

	def me(self, request, *args, **kwargs):
		self.object = get_object_or_404(myModels.User, pk=request.user.id)
		serializer = self.get_serializer(self.object)
		return Response(serializer.data)

class LoginView(APIView):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'login.html'

	def get(self, request):
		return Response()
	
	def post(self, request):
		serializer = serializers.UserLoginSerializer(data=request.data)
		if serializer.is_valid():
			user = authenticate(username=request.data['username'], password=request.data["password"])
			if user:
				print("AAAA")
				login(request, user)
				return Response(status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)

class	UserRegisterAPIView(APIView):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'register.html'
	
	def sing_up_succesfull_response(self, serializer):
		response = {
			'success': True,
			'user': serializer.data,
		}
		return (response)

	def get(self, request):
		return Response()

	def post(self, request):
		serializer = serializers.RegisterSerializer(data=request.data)
		if (serializer.is_valid()):
			serializer.save()
			response = self.sing_up_succesfull_response(serializer)
			return Response(response, status=status.HTTP_200_OK)
		raise ValidationError(serializer.errors, code=status.HTTP_406_NOT_ACCEPTABLE)