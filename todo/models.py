from django.db import models

# Create your models here.

class ToDo(models.Model):
	Title = models.CharField(max_length=200)
	Description = models.CharField(max_length=200)
	Duration = models.CharField(max_length=200)
	Venue = models.CharField(max_length=200)

	def _str_(self):
		return self.Title

class Admin:
	pass


