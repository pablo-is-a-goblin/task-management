from rest_framework import serializers
from . import models as myModels
from rest_framework.exceptions import ValidationError

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = myModels.Tag
        fields = ['id', 'name', 'description']

class TaskSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=myModels.Tag.objects.all())
    assigned_to = serializers.PrimaryKeyRelatedField(many=True, queryset=myModels.User.objects.all())
    
    class Meta:
        model = myModels.Task
        fields = ['id', 
                  'title', 
                  'description',
                  'status',
                  'priority',
                  'tags',
                  'estimated_hours',
                  'actual_hours',
                  'due_date',
                  'assigned_to',
                  'is_archived',
                  'created_by',
                  ]
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = myModels.User
        fields = ['id', 'username']
    
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = myModels.User
        fields = ['id', 'username', 'email', 'password',]

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