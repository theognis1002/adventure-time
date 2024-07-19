import json
import logging
import os

from django.apps import apps
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework.authtoken.models import Token

LOGGER = logging.getLogger("root")
User = get_user_model()
Story = apps.get_model("stories", "Story")
Frame = apps.get_model("stories", "Frame")
Button = apps.get_model("stories", "Button")

DEFAULT_USERNAME = "johndoe1"
DEFAULT_EMAIL = "johndoe@gmail.com"
DEFAULT_PASSWORD = "foo"
FIXTURE_DIR = os.path.join(settings.BASE_DIR, "data")


class SetupManager:

    @transaction.atomic
    def setup_users(self):
        if not User.objects.all().exists():
            User.objects.create_user(username=DEFAULT_USERNAME, email=DEFAULT_EMAIL, password=DEFAULT_PASSWORD)
            LOGGER.info("User created successfully!")

    @transaction.atomic
    def setup_tokens(self):
        user = User.objects.first()
        token, created = Token.objects.get_or_create(user=user, key="opensesame")
        if created:
            LOGGER.info("Token created successfully!")

    @transaction.atomic
    def setup_stories(self):
        LOGGER.info("Story created successfully!")
        story, created = Story.objects.get_or_create(title="There and Back Again")
        if created:
            LOGGER.info("Story created successfully!")

        with open(os.path.join(FIXTURE_DIR, "story.json")) as file:
            data = json.load(file)

        for idx, frame_data in enumerate(data["frames"]):
            buttons = frame_data.pop("buttons", [])
            frame, created = Frame.objects.update_or_create(story=story, index=idx, defaults=frame_data)
            if created:
                LOGGER.info("%s created successfully!", frame)

            for button_data in buttons:
                link_index = button_data.pop("linkindex")
                button, created = Button.objects.update_or_create(frame=frame, link_index=link_index, defaults=button_data)
                if created:
                    LOGGER.info("%s created successfully!", button)

    def execute(self):
        self.setup_users()
        self.setup_tokens()
        self.setup_stories()


def run():
    setup = SetupManager()
    setup.execute()
