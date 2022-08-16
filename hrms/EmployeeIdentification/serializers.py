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


