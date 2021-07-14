from rest_framework import serializers
from .models import Profile
from hint.models import Theme

class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ('id', 'name', 'enterKey')

class ProfileSerializer(serializers.ModelSerializer):
    themes = ThemeSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'user', 'escape_room', 'reset', 'phone', 'themes')

