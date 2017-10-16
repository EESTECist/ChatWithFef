from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    is_bot = models.BooleanField(default=0)
    #user = models.ForeignKey(User, blank=False, null=False)

    def __str__(self):
        return "{} : (is bot? {}) : {}".format(self.message, self.is_bot, self.timestamp.date())
