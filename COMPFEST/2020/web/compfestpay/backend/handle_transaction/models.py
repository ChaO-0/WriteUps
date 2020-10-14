

from django.db import models
from django.contrib.auth.models import User


class Transaction(models.Model):
	to_user = models.TextField()
	from_user = models.TextField()
	amount = models.BigIntegerField()
