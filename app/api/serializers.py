from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Thing

UserModel = get_user_model()


class ThingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Thing
        fields = ['id', 'name']

    def create(self, validated_data):
        user = self.context['request'].user
        thing = Thing.objects.create(user=user, **validated_data)
        return thing


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'username', 'email']
