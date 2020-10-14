

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import os, codecs


def random_signature():
	return codecs.encode(os.urandom(32), 'hex').decode('utf-8')

class UserWallet(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	value = models.BigIntegerField(default=1)
	signature = models.TextField(default=random_signature)

@receiver(post_save, sender=User)
def create_wallet(sender, instance, created, **kwargs):
	if created:
		wallet = UserWallet.objects.create(user=instance)
		wallet.save()

@receiver(post_save, sender=User)
def save_wallet(sender, instance, **kwargs):
	instance.userwallet.save()