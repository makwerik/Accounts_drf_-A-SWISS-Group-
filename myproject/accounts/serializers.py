from .models import Users
from rest_framework import serializers


class UsersSerializer(serializers.ModelSerializer):
    """Сериализатор юзеров"""

    class Meta:
        model = Users
        fields = '__all__'
