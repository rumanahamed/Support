from rest_framework import serializers


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
    relationship = serializers.CharField(max_length=100)
    contactNumber = serializers.IntegerField()
    Address = serializers.CharField(max_length=100)


class postEmployeeBankDataSerializer(serializers.Serializer):
    AccountType = serializers.CharField(max_length=100)
    AccountName = serializers.CharField(max_length=100)
    IFSCCode = serializers.CharField(max_length=100)
    BankName = serializers.CharField(max_length=100)
    AccountNumber = serializers.IntegerField()

class updateEmployeeBankDataSerializer(serializers.Serializer):
    AccountType = serializers.CharField(max_length=100,required=False)
    AccountName = serializers.CharField(max_length=100,required=False)
    IFSCCode = serializers.CharField(max_length=100,required=False)
    BankName = serializers.CharField(max_length=100,required=False)
    AccountNumber = serializers.IntegerField(required=False)