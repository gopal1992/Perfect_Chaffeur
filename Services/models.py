from django.db import models

# Create your models here.
class Customer(models.Model):
    Login_Name=models.CharField(max_length=20)
    Full_Name=models.CharField(max_length=20)
    Email_Id=models.CharField(max_length=30)
    Password=models.CharField(max_length=10)
    Phone_Number=models.IntegerField()
    Gender=models.CharField(max_length=10)
    Date_of_Birth=models.IntegerField()
    Nationality=models.CharField(max_length=30)
    Address=models.CharField(max_length=100)
    City=models.CharField(max_length=30)
    Country=models.CharField(max_length=20)
    State=models.CharField(max_length=20)
    Postal_Code=models.CharField(max_length=10)
    ID_Card_Type=models.CharField(max_length=30)
    ID_Card_Number=models.CharField(max_length=30)
    Issuing_Authority=models.CharField(max_length=30)

      
class Login(models.Model):
	username = models.CharField(max_length=20, unique=True)
	password = models.CharField(max_length=20)

	def __unicode__(self):
		return self.usernamet
class List_of_fligths(models.Model):
    Fligth_No=models.CharField(max_length=10)
    Fligth_Name=models.CharField(max_length=10)
    From=models.CharField(max_length=15)
    To=models.CharField(max_length=15)
    Date=models.CharField(max_length=15)


    
    
