from django.db import models


class Person(models.Model):
	
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	
	@property
	def full_name(self):
		return '{} {}'.format(self.first_name, self.last_name)
