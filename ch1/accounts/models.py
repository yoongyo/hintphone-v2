from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save

Nation = (
    ('Korea', 'Korea'),
    ('Japan', 'Japan'),
    ('China', 'China'),
)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nation = models.CharField(max_length=30, choices=Nation, blank=True, null=True)
    escape_room = models.CharField(max_length=30)
    reset = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    textHint = models.BooleanField(default=True)
    answer = models.BooleanField(default=False)
    money = models.CharField(max_length=30, blank=True, null=True)
    timer = models.BooleanField(default=False)
    pause = models.BooleanField(default=False)
    onlyCode = models.BooleanField(default=False)

    def __str__(self):
        return self.escape_room

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance, user_pk=instance.id)
#
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()