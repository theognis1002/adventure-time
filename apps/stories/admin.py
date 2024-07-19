from django.contrib import admin

from .models import Button, Frame, Story


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "modified")
    search_fields = ("title",)
    ordering = ("title",)
    list_filter = ("created", "modified")


@admin.register(Frame)
class FrameAdmin(admin.ModelAdmin):
    list_display = ("story", "index", "title", "created", "modified")
    search_fields = ("title", "body", "story__title")
    ordering = ("story", "index")
    list_filter = ("story", "created", "modified")


@admin.register(Button)
class ButtonAdmin(admin.ModelAdmin):
    list_display = ("frame", "text", "link_index", "created", "modified")
    search_fields = ("text", "frame__title", "frame__story__title")
    ordering = ("frame", "link_index")
    list_filter = ("frame", "created", "modified")
    ordering = ("frame", "link_index")
    list_filter = ("frame", "created", "modified")
