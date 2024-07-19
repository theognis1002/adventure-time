from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel, UUIDModel


class Story(UUIDModel, TimeStampedModel):
    title = models.CharField(_("Story Title"), max_length=125)

    class Meta:
        verbose_name = _("Story")
        verbose_name_plural = _("Stories")

    def __str__(self) -> str:
        return f"Story ID#{self.pk} - {self.title}"


class Frame(TimeStampedModel):
    story = models.ForeignKey(Story, related_name="frames", on_delete=models.CASCADE, verbose_name=_("Story"))
    index = models.PositiveSmallIntegerField(_("Index"))
    title = models.CharField(_("Title"), max_length=125)
    body = models.TextField(_("Body"))
    img = models.URLField(_("Image URL"), blank=True, null=True)
    colors = models.JSONField(default=dict, blank=True, null=True, encoder=DjangoJSONEncoder)

    class Meta:
        unique_together = ("story", "index")  # per requirement
        verbose_name = _("Frame")
        verbose_name_plural = _("Frames")

    def __str__(self) -> str:
        return f"Frame ID#{self.pk}"


# debated just adding this as an `ArrayField` / `JSONField on `Frame` - decided to put it as a separate `Button` model instead.
# It could be implemented either way.
class Button(TimeStampedModel):
    frame = models.ForeignKey(Frame, related_name="buttons", on_delete=models.CASCADE, verbose_name=_("Frame"))
    text = models.CharField(_("Button Text"), max_length=255)
    link_index = models.PositiveSmallIntegerField(_("Link Index"))

    class Meta:
        verbose_name = _("Button")
        verbose_name_plural = _("Buttons")

    def __str__(self) -> str:
        return f"Button ID#{self.pk}"
