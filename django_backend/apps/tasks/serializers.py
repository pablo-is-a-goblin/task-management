from rest_framework import serializers
from . import models as myModels
from rest_framework.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = myModels.User
        fields = ['id', 'username']
    
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = myModels.User
        fields = ['id', 'username', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user, created = myModels.User.objects.update_or_create(
            username=validated_data['username'], 
            defaults=validated_data)
        if not created:
            ValidationError({"detail": "Can't create user"})
        user.set_password(password)
        user.save()
        return (user)


class UserLoginSerializer(serializers.ModelSerializer):
	username = serializers.CharField(write_only=True)
	password = serializers.CharField(write_only=True)

	class Meta:
		model = myModels.User
		fields = [
			"username",
			"password"
		]