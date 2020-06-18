from django.db import models

# Create your models here.
class Blog(models.Model):
		name=models.CharField(max_length=100)
		data=models.CharField(max_length=100)
		date=models.DateField()
		
	
		def __str__(self):
			return self.name