from django.db import models

# Create your models here.
class Attendee(models.Model):
  name = models.CharField(max_length=100)
  phone = models.CharField(max_length=50)
  address = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=100)
  country = models.CharField(max_length=100)
  postalZip = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  Company = models.CharField(max_length=100)
  companyFunded = models.CharField(max_length=100)
  userID = models.CharField(max_length=500)
  team = models.CharField(max_length=100)
  paid = models.CharField(max_length=100)
  date = models.CharField(max_length=100)
  title = models.CharField(max_length=100)

  def __str__(self):
    return f"{self.name}"