from rest_framework import serializers
from .models import *

class EmployeeOnboardSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100)


class updateEmployeeDataSerializer(serializers.Serializer):
    Mobile = serializers.IntegerField()
    HomeAddress = serializers.CharField(max_length=100,allow_blank=True,required=False)
    WorkEmail = serializers.EmailField(allow_blank=True,allow_null=True)
    Gender = serializers.CharField(max_length=100,allow_blank=True,allow_null=True)


class postEmployeeFamilyDataSerializer(serializers.Serializer):
    relationshipName = serializers.CharField(max_length=100)
    relationshipType = serializers.CharField(max_length=100)
    contactNumber = serializers.IntegerField()
    Address = serializers.CharField(max_length=100)


class updateEmployeeFamilyDataSerialzer(serializers.Serializer):
    relationshipId = serializers.IntegerField()
    relationshipName = serializers.CharField(max_length=100,required=False)
    relationshipType = serializers.CharField(max_length=100,required=False)
    contactNumber = serializers.IntegerField(required=False)
    Address = serializers.CharField(max_length=100,required=False)


class postEmployeeBankDataSerializer(serializers.Serializer):
    AccountType = serializers.CharField(max_length=100)
    AccountName = serializers.CharField(max_length=100)
    IFSCCode = serializers.CharField(max_length=100)
    BankName = serializers.CharField(max_length=100)
    AccountNumber = serializers.IntegerField()


class updateEmployeeBankDataSerializer(serializers.Serializer):
    AccountNumber = serializers.IntegerField(required=False)


class postEmployeeLanguageDataSerializer(serializers.Serializer):
    language = serializers.CharField(max_length=100)
    proficientLevel = serializers.CharField(max_length=100)


class postEmployeeLeaveCreditSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    leaveType = serializers.CharField(max_length=100)
    leaveCount = serializers.IntegerField()
    month = serializers.CharField(max_length=100)


class EmployeeProfileMenuSerializer(serializers.Serializer):
    menu = serializers.CharField(max_length=100)


class postEmployeequalificationDataSerializer(serializers.Serializer):
    QualificationType = serializers.CharField(max_length=100)
    Board = serializers.CharField(max_length=100)
    certificate_no = serializers.CharField(max_length=100)
    Year_of_passing = serializers.CharField(max_length=4)
    Institute = serializers.CharField(max_length=100)
    Location = serializers.CharField(max_length=100)
    Percentage = serializers.FloatField()

class postEmployeeworkDataSerializer(serializers.Serializer):
    companyName = serializers.CharField(max_length=100)
    Location = serializers.CharField(max_length=100)
    Role = serializers.CharField(max_length=100)
    YearOfExperience = serializers.CharField(max_length=100)


class postEmployeelanguageSerializer(serializers.Serializer):
    language = serializers.CharField(max_length=100)
    read = serializers.CharField(max_length=100)
    write = serializers.CharField(max_length=100)
    speak = serializers.CharField(max_length=100)


class postEmployeeRoleDataSerializer(serializers.Serializer):
    Role = serializers.CharField(max_length=100)


class postEmployeeprojectSerializer(serializers.Serializer):
    projectName = serializers.CharField(max_length=100)
    clientName = serializers.CharField(max_length=100)
    duration = serializers.FloatField()
    status = serializers.BooleanField()
    projectStartDate = serializers.DateField()
    projectManager = serializers.CharField(max_length=100)
    technology = serializers.JSONField()

class postEmployeeLeaveApplyserializer(serializers.Serializer):
    leaveType = serializers.CharField(max_length=100)
    leaveDescription = serializers.CharField(max_length=100)
    attachment = serializers.FileField(required=False)
    from_date = serializers.DateField()
    to_date = serializers.DateField()


class postEmployeeLeaveApproveserializer(serializers.Serializer):
    empid = serializers.CharField(max_length=100)
    leaveId = serializers.CharField(max_length=100)
    statusData = serializers.CharField(max_length=100)

