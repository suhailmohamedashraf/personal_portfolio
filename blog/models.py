from django.db import models

class BlogProject(models.Model):

	title = models.CharField(max_length=100)
	date = models.DateField(auto_now=False, auto_now_add=False)
	description = models.CharField(max_length=500)



	def __str__(self):
		return self.title