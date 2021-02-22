from rest_framework import serializers
from .models import Todo




class DisplayTodoSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields =  '__all__'

class RegisterTodo(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    priority = serializers.CharField()

    