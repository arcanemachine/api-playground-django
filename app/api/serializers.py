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

    def validate(self, data):
        obj = self.instance
        user = self.context['request'].user

        user_things = Thing.objects.filter(user=user)

        # do not allow a user to have duplicate thing names
        if user_things.filter(name=data['name']).first() != obj:
            raise serializers.ValidationError(
                {'name': "You already have a Thing with this name."},
                code="thing_name_duplicate")

        return data


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'username', 'email']
