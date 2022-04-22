from rest_framework import serializers

from .models import Thing


class ThingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Thing
        fields = ['id', 'name']

    def create(self, validated_data):
        user = self.context['request'].user
        thing = Thing.objects.create(user=user, **validated_data)
        return thing
