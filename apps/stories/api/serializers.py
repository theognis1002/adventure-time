from rest_framework import serializers
from stories.models import Button, Frame, Story


class StoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ["id"]


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = "__all__"


class ButtonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Button
        fields = "__all__"


class FrameSerializer(serializers.ModelSerializer):
    buttons = ButtonSerializer(many=True)

    class Meta:
        model = Frame
        fields = "__all__"
