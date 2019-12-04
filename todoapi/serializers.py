from rest_framework import serializers
from .models import Todoapi

class TodoSerializer(serializers.ModelSerializer):
    
    # tags = TagSerializer(many=True, required=False, read_only=True)
    # author = UserSerializer(required=False, read_only=True)
    # serializers.ImageField(use_url=True, required=False, allow_null=True)

    class Meta:
        model = Todoapi
        fields = '__all__' #fields = ['user', 'title', 'completed']
        # read_only_fields = ('created_at',)
