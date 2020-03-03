from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length = 30, null=True, blank = True)

    def __str__(self):
        return self.user.username


def post_save_profile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        try:
            Profile.objects.create(user = instance)
        except:
            pass

post_save.connect(post_save_profile_receiver, sender = User)
