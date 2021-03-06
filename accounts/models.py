from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
	locations = (
		('Home', 'Home'),
	)
	access_levels = (
		('Sales', 'Sales'), ('Drivers', 'Drivers'), ('Management', 'Management'), ('Admin', 'Admin'),
	)
	contact_number = models.CharField(max_length=12, unique=True)
	location = models.CharField(max_length=4, choices=locations, default='Home')
	access_level = models.CharField(max_length=10, choices=access_levels, default='Sales')
