from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

User = settings.AUTH_USER_MODEL

class Airline(models.Model):
    airline = models.CharField(max_length=255)

    def __str__(self):
        return self.airline


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'Профиль пользователя {self.user.username}'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
