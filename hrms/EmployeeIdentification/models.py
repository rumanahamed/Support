from django.db import models
#####Token Authentication####
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User #butiln User tABLE
#####Token Authentication####

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Employee(models.Model):
    empid = models.ForeignKey(User,on_delete=models.CASCADE)
    password = models.CharField(max_length=100)
    Name = models.CharField(max_length=100,blank=True,null=True)
    Photo = models.CharField(max_length=100,blank=True,null=True)
    Mobile = models.IntegerField(blank=True,null=True)
    OfficePhone = models.IntegerField(null=True,blank=True)
    HomeAddress = models.CharField(max_length=100,blank=True,null=True)
    WorkAddress = models.CharField(max_length=100,blank=True,null=True)
    AdharCard = models.CharField(max_length=100,blank=True,null=True)
    Pancard = models.CharField(max_length=100,blank=True,null=True)
    Passport = models.CharField(max_length=100, default='',null=True,blank=True)
    WorkEmail = models.CharField(max_length=100,blank=True,null=True)
    Designation = models.CharField(max_length=100,blank=True,null=True)
    AboutMe = models.CharField(max_length=100, default='',null=True,blank=True)
    JoiningDate = models.DateTimeField(blank=True,null=True)
    CreatedDate = models.DateTimeField(blank=True,null=True)
    FirstName = models.CharField(max_length=50,blank=True,null=True)
    lastName = models.CharField(max_length=50,blank=True,null=True)
    Location = models.CharField(max_length=100,blank=True,null=True)
    DOB = models.DateTimeField(blank=True,null=True)
    Gender = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.Name


class FamilyEmergencyContacts(models.Model):
    empid = models.ForeignKey(User, on_delete=models.CASCADE)
    relationshipId = models.AutoField(primary_key=True)
    relationship = models.CharField(max_length=100)
    contactNumber = models.IntegerField()
    Address = models.CharField(max_length=100)

    def __str__(self):
        return self.Address


AccountTypeData = (("Salary Account","Salary Account"),
                   ("PPF Account","PPF Account"))
class EmployeeBankDetails(models.Model):
    empid = models.ForeignKey(User, on_delete=models.CASCADE)
    AccountType = models.CharField(max_length=100,choices=AccountTypeData)
    AccountName = models.CharField(max_length=100)
    IFSCCode = models.CharField(max_length=100)
    BankName = models.CharField(max_length=100)
    AccountNumber = models.IntegerField()

    def __str__(self):
        return self.AccountType

