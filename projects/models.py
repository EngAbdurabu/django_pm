from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField()

	def __str__(self):
		return self.name


