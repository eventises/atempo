from django.db import models

# Create your models here.
class Atempo(models.Model):
	name = models.CharField(max_length=128)
	email = models.CharField(max_length=128)
	message = models.TextField(blank=True, null=True)