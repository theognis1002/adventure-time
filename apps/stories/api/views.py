import logging

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

# from rest_framework.decorators import action
# from rest_framework.response import Response
from stories.models import Frame, Story

from .serializers import FrameSerializer, StoryListSerializer, StorySerializer

LOGGER = logging.getLogger("root")


class StoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Story.objects.prefetch_related("frames").all()
    list_serializer_class = StoryListSerializer
    serializer_class = StorySerializer
    authentication_classes = [TokenAuthentication]

    def get_serializer_class(self):
        if self.action == "list":
            return self.list_serializer_class
        return self.serializer_class

    # @action(detail=True, methods=["get"])
    # def frames(self, request, pk=None, **kwargs):
    #     instance = self.get_object()
    #     index = request.query_params.get("index")

    #     if index is not None:
    #         try:
    #             index = int(index)
    #             frame = instance.frames.get(index=index)
    #             serializer = FrameSerializer(frame)
    #             return Response(serializer.data)
    #         except (ValueError, Frame.DoesNotExist):
    #             return Response({"detail": "Frame not found."}, status=404)

    #     serializer = FrameSerializer(instance.frames.all(), many=True)
    #     return Response(serializer.data)


class FrameViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FrameSerializer
    authentication_classes = [TokenAuthentication]
    lookup_field = "index"

    def get_queryset(self):
        story_id = self.kwargs["story_pk"]
        return Frame.objects.filter(story_id=story_id)
