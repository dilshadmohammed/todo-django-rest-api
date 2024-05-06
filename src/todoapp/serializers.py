from rest_framework import serializers
from .models import Todo
from django.contrib.auth.models import User

class TodoSerializer(serializers.ModelSerializer):
    status = serializers.CharField(max_length=20, read_only=True)
    class Meta:
        model = Todo
        exclude = ['owner']
    def create(self, validated_data):
        user_id = self.context['request'].user.id
        user = User.objects.get(id=user_id)
        return Todo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('task', instance.task)
        
        instance.save()
        return instance
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
