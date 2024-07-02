from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
class Record(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	email =  models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	address =  models.CharField(max_length=100)
	department =  models.CharField(max_length=50)
	role =  models.CharField(max_length=50)
	dob =  models.DateField()

	def __str__(self):
		return(f"{self.first_name} {self.last_name}")


@receiver(pre_save, sender=Record)
def set_owner_on_creation(sender, instance, **kwargs):
	if instance.pk is None:
		instance.owner = instance.owner or User.objects.get(username="soumya")
