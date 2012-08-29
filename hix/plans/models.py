from django.db import models
import PIL


# Create your models here.

class InsurnaceCo(models.Model):
  insuranceconame = models.CharField(max_length=200)
  insurancecoaddress1 = models.CharField(max_length=200)
  insurancecoadress2 = models.CharField(max_length=200)
  insurancecocity = models.CharField(max_length=200)
  insurancecostate = models.CharField(max_length=20)
  insurancecozip = models.CharField(max_length=10)
  insurancecophone = models.CharField(max_length=13)
  insurancecowebsite = models.CharField(max_length=200)
  insurancecopublicemail = models.EmailField(max_length=254)
  insurancecoadminemail = models.EmailField(max_length=254)
  #insurancecologo = models.ImageField(upload_to=


class Plans(models.Model):
  description = "The plans available (or potentially available) in the exchange"
  
  insuranceco = models.ForeignKey(InsuranceCo)
  planname = models.CharField(max_length=200)
  approved = models.BooleanField
  dateaplanpproved = models.DateTimeField
  
