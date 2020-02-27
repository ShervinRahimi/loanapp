from django.db import models

class RequestHeader(models.Model):

    CFRequestId = models.CharField(max_length = 200)
    RequestDate = models.DateTimeField()
    FApiUserId = models.CharField(max_length = 200, blank = True, null = True)
    CFApiPassword = models.CharField(max_length = 200, blank = True, null = True)
    IsTestLead = models.BooleanField(null = True)

class Business(models.Model):
    name = models.CharField(max_length=200)
    annual_revenue = models.FloatField()
    MonthlyAverageBankBalance = models.FloatField()
    AvgCreditVolume = models.FloatField()
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200,blank=True,null=True)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip = models.IntegerField(blank=True)
    tax_id = models.IntegerField(blank=True)
    phone = models.IntegerField(blank=True)
    naics = models.IntegerField(blank=True)
    has_been_profitable = models.BooleanField()
    bankrupted = models.BooleanField()
    inception_date = models.DateField()

class Owners(models.Model):
    name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200,blank=True,null=True)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip = models.IntegerField(blank=True)
    dob = models.DateTimeField()
    phone = models.IntegerField(blank=True)
    ssn = models.IntegerField(blank=True)
    percentOwnership = models.FloatField()

class CFAData(models.Model): 
    requestAmount = models.IntegerField(blank=True)
    statedCreditHistory = models.FloatField()
    legalEntityType = models.CharField(max_length=200)
    filterID = models.IntegerField(blank=True)

class Address(models.Model):
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200,blank=True,null=True)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip = models.IntegerField(blank=True)
    




    


