from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter
from stories.api.views import FrameViewSet, StoryViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

# stories
router.register("stories", StoryViewSet, basename="stories")
stories_router = NestedSimpleRouter(router, r"stories", lookup="story")
stories_router.register(r"frames", FrameViewSet, basename="frames")

app_name = "api"
urlpatterns = [
    path(r"", include(router.urls)),
    path(r"", include(stories_router.urls)),
]
