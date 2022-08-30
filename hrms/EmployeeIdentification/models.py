from django.db import models
#####Token Authentication####
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User #butiln User tABLE
import datetime
#####Token Authentication####

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Employee(models.Model):
    empid = models.ForeignKey(User,on_delete=models.CASCADE)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=100,primary_key=True)
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
        return self.username


class FamilyEmergencyContacts(models.Model):
    empid = models.ForeignKey(User, on_delete=models.CASCADE)
    relationshipId = models.AutoField(primary_key=True)
    relationshipName = models.CharField(max_length=100)
    relationshipType = models.CharField(max_length=100)
    contactNumber = models.IntegerField(unique=True)
    Address = models.CharField(max_length=100)

    def __str__(self):
        return str(self.relationshipId)

boardTypeData = (("Intermediate", "Intermediate"),
                 ("Graduation", "Graduation"),("Post Graduation","Post Graduation")
                 )
class Employeequalification(models.Model):
    empid = models.ForeignKey(User, on_delete=models.CASCADE)
    QualificationType = models.CharField(max_length=100, choices=boardTypeData)
    Board = models.CharField(max_length=100)
    Year_of_passing = models.CharField(max_length=4)
    certificate_no = models.CharField(max_length=100,unique=True)
    Institute = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    Percentage = models.FloatField()

    def str(self):
        return self.QualificationType


workTypeData = (("Management", "Management"),
                ("Frontend", "Frontend"),
                ("Backend", "Backend"),
                ("Testing", "Testing"))


class Workexperience(models.Model):
    empid = models.ForeignKey(User, on_delete=models.CASCADE)
    workId = models.AutoField(primary_key=True)
    companyName = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    Role = models.CharField(max_length=100,choices=workTypeData)
    YearOfExperience = models.FloatField()

    def _str_(self):
        return self.companyName


proficientLevelData = (
                        ("HIGH", "HIGH"),
                        ("MEDIUM", "MEDIUM"),
                        ("LOW", "LOW")
                      )


class EmployeeLanguage(models.Model):
    empid = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.CharField(max_length=100,unique=True)
    speak = models.CharField(max_length=100, choices=proficientLevelData)
    read = models.CharField(max_length=100, choices=proficientLevelData)
    write = models.CharField(max_length=100, choices=proficientLevelData)

    def _str_(self):
        return self.language


class EmployeeRole(models.Model):
    empid = models.ForeignKey(User, on_delete=models.CASCADE)
    Role = models.CharField(max_length=100,primary_key=True)
    status = models.BooleanField(default=True)

    def _str_(self):
        return self.Role

AccountTypeData = (("Salary Account","Salary Account"),
                   ("PPF Account","PPF Account"))


class EmployeeBankDetails(models.Model):
    empid = models.ForeignKey(User, on_delete=models.CASCADE)
    AccountType = models.CharField(max_length=100,choices=AccountTypeData)
    AccountName = models.CharField(max_length=100)
    IFSCCode = models.CharField(max_length=100)
    BankName = models.CharField(max_length=100)
    AccountNumber = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.AccountType


class EmployeeProjectDetails(models.Model):
    empid = models.ForeignKey(User, on_delete=models.CASCADE)
    projectName = models.CharField(max_length=100)
    clientName = models.CharField(max_length=100)
    duration = models.FloatField()
    status = models.BooleanField()
    projectStartDate = models.DateField()
    projectManager = models.CharField(max_length=100)
    technology = models.TextField()

    def _str_(self):
        return self.projectName


leaveTypeData = (
    ("CasualLeave","CasualLeave"),
    ("SickLeave","SickLeave"),
    ("PrevilageLeave","PrevilageLeave")
)
leaveStatusData = (
    ("Approved","Approved"),
    ("Pending","Pending"),
    ("Canceled","Canceled")
)


class EmployeeApplyLeave(models.Model):
    empid = models.ForeignKey(User, on_delete=models.CASCADE)
    leaveId = models.AutoField(primary_key=True)
    leaveType = models.CharField(max_length=100,choices=leaveTypeData)
    leaveDescription = models.CharField(max_length=100)
    leaveStatus = models.CharField(max_length=100,choices=leaveStatusData,default="Pending")
    attachment = models.FileField(upload_to="uploads",null=True,blank=True)
    assigne = models.CharField(max_length=100)
    from_date = models.DateField(null=True,blank=True)
    to_date = models.DateField(null=True,blank=True)
    leaveCount = models.FloatField(default=0)

    def __str__(self):
        return self.leaveStatus



class EmployeeCreditLeaveData(models.Model):
    empid = models.ForeignKey(User, on_delete=models.CASCADE)
    leaveType = models.CharField(max_length=100, choices=leaveTypeData)
    leaveCount = models.IntegerField()
    datetime = models.DateTimeField(default=datetime.datetime.now())
    month = models.CharField(max_length=100)

    def __str__(self):
        return self.leaveType


class EmployeeTotalLeaveData(models.Model):
    empid = models.ForeignKey(User, on_delete=models.CASCADE)
    leaveType = models.CharField(max_length=100, choices=leaveTypeData,null=True,blank=True)
    TotalleaveCount = models.IntegerField(default=0)
    datetime = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        data = str(self.leaveType) + "_" + str(self.empid)
        return data


ticketStatusData = (
    ("Unassigned Tickets","Unassigned Tickets"),
    ("Open Tickets","Open Tickets"),
    ("Solved Tickets","Solved Tickets")
)

ticketCategoryData = (
    ("HR","HR"),
    ("IT","IT"),
    ("Salary","Salary"),
    ("Other","Other"),
    ("Admin","Admin")
)


class EmployeeTicket(models.Model):
    empid = models.ForeignKey(User,on_delete=models.CASCADE)
    ticketId = models.AutoField(primary_key=True)
    ticketDescription = models.CharField(max_length=100)
    category = models.CharField(max_length=100,choices=ticketCategoryData)
    attachment = models.CharField(max_length=100,null=True,blank=True)
    status = models.CharField(max_length=100,choices=ticketStatusData,default="Unassigned Tickets")
    assigne = models.CharField(max_length=100,default="a649116")

    def __str__(self):
        return self.ticketDescription


class EmployeeAnnouncement(models.Model):
    empid = models.ForeignKey(User, on_delete=models.CASCADE)
    Image = models.CharField(max_length=100,null=True,blank=True)
    Date = models.DateTimeField(default=datetime.datetime.now())
    Announcement = models.TextField()

    def _str_(self):
        return self.Announcement


SkillTypeData = (
    ("Beginner","Beginner"),
    ("Intermediate","Intermediate"),
    ("Advanced","Advanced"))


class SkillManagement(models.Model):
    empid = models.ForeignKey(User, on_delete=models.CASCADE)
    SkillId = models.AutoField(primary_key=True)
    SkillName = models.CharField(max_length=100)
    ProficientLevel=models.CharField(max_length=100,choices=SkillTypeData)
    Experience=models.FloatField()
    LastUsed = models.CharField(max_length=100)

    def __str__(self):
        return self.SkillName