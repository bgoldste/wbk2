from django.db import models

# Create your models here.
class Subscriber(models.Model):
	email_address = models.EmailField()