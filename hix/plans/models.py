from django.db import models
#import PIL
#PIL needed for logo


# Create your models here.

class InsurnaceCo(models.Model):
  insuranceconame = models.CharField(max_length=200)
  insurancecoaddress1 = models.CharField(max_length=200)
  insurancecoadress2 = models.CharField(max_length=200)
  insurancecocity = models.CharField(max_length=200)
  insurancecostate = models.CharField(max_length=20)
  insurancecozip = models.CharField(max_length=10)
  insurancecophone = models.CharField(max_length=13)
  insurancecowebsite = models.URLField(max_length=200)
  insurancecopublicemail = models.EmailField(max_length=254)
  insurancecoadminemail = models.EmailField(max_length=254)
  #insurancecologo = models.ImageField(upload_to=
  def __unicode__(self):
        return self.insuranceconame


class Plans(models.Model):
  description = "The plans available (or potentially available) in the exchange"
  
  #insuranceco = models.ForeignKey(InsuranceCo)
  planname = models.CharField(max_length=200)
  approved = models.BooleanField()
  dateaplanpproved = models.DateTimeField()
  planprice = models.DecimalField(max_digits=8, decimal_places=2)
  def __unicode__(self):
        return self.planname

  
  #maybe these should be constants? since there will only be one per?
  #FPL  federal poverty level = $11,172 for individual
class Exchange(models.Model):
  exchangename = models.CharField(max_length=200)
  exchangeaddress1 = models.CharField(max_length=200)
  exchangeadress2 = models.CharField(max_length=200)
  exchangecity = models.CharField(max_length=200)
  exchangestate = models.CharField(max_length=20)
  exchangezip = models.CharField(max_length=10)
  exchangephone = models.CharField(max_length=13)
  exchangewebsite = models.URLField(max_length=200)
  exchangepublicemail = models.EmailField(max_length=254)
  exchangeadminemail = models.EmailField(max_length=254)
  #exchangelogo = models.ImageField(upload_to=
  #what legislation or executive order created this exchange
  exchangelegalauirization = models.URLField(max_length=200)
  exchangevisionstatement = models.CharField(max_length=254)
  #by ACA must be at 
  exchangemaxemployees = models.IntegerField()
  exchangeinsurancecommission = models.URLField(max_length=200)
  def __unicode__(self):
        return self.exchangename
  
class ExchangeBoard(models.Model):
  #exchange = models.ForeignKey('Exchange')
  exchangeboardmembername = models.CharField(max_length=200)
  exchangeboardmembertitle = models.CharField(max_length=200)
  exchangeboardmemberbio = models.CharField(max_length=512)
  #exchangeboardprofilepic = models.ImageField(upload_to=
  def __unicode__(self):
        return self.exchangeboardmembername