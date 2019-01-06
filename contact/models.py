from django.db import models

# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField()
	content = models.TextField()
	phone = models.CharField(max_length=120, blank=True, null=True)

	class Meta:
		verbose_name = 'Contact Message'
		verbose_name_plural = 'Contact Messages'
			