from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from .serializers import *
from django.contrib.auth.models import User
from .models import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class EmployeeOnboardRegister(APIView):
    def post(self,request):
        try:
            serializer = EmployeeOnboardSerializer(data= request.data)
            if serializer.is_valid():
                username = serializer.data['username']
                email = serializer.data['email']
                password = serializer.data["password"]
                User.objects.create_user(username=username, password=password,email=email)

                data = User.objects.filter(username=username).values()[0]
                id = data["id"]

                Employee.objects.create(
                    empid_id = id,
                    password = password,
                    Name = username

                )
                data = {'Message': "Employee Onboard Successfully"}
                return JsonResponse(data, safe=False)
            return JsonResponse(serializer.errors, safe=False)
        except Exception as e:
            return JsonResponse(str(e), safe=False)


class updateEmployeeData(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        try:
            serializer = updateEmployeeDataSerializer(data= request.data)
            if serializer.is_valid():
                print(serializer.data)
                print("username=",request.user)
                data = User.objects.filter(username=request.user).values()[0]
                id = data["id"]

                Employee.objects.filter(empid=id).update(
                    **serializer.data
                )

                data = {'Message': "Employee Data Updated Successfully"}
                return JsonResponse(data, safe=False)
            return JsonResponse(serializer.errors, safe=False)
        except Exception as e:
            return JsonResponse(str(e), safe=False)


class getEmployeeData(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        try:
            Userdata = User.objects.filter(username=request.user).values()[0]
            id = Userdata["id"]
            employee_data = Employee.objects.filter(empid=id).values()[0]
            result = {}
            result["Name"] = employee_data["Name"]
            result["Mobile"] = employee_data["Mobile"]
            result["HomeAddress"] = employee_data["HomeAddress"]
            result["WorkEmail"] = employee_data["WorkEmail"]
            result["Gender"] = employee_data["Gender"]

            data = {
                    'Message': "Employee Details",
                    "data": result
                    }
            return JsonResponse(data, safe=False)
        except Exception as e:
            return JsonResponse(str(e), safe=False)


class postEmployeeFamilyData(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            serializer = postEmployeeFamilyDataSerializer(data=request.data)
            if serializer.is_valid():
                relationship = serializer.data['relationship']
                contactNumber = serializer.data['contactNumber']
                Address = serializer.data['Address']

                print("username=", request.user)
                data = User.objects.filter(username=request.user).values()[0]
                id = data["id"]

                FamilyEmergencyContacts.objects.create(
                    empid_id = id,
                    relationship=relationship,
                    contactNumber=contactNumber,
                    Address=Address
                )

                data = {'Message': "Employee Family & Emergency Contacts Updated Successfully"}
                return JsonResponse(data, safe=False)
            return JsonResponse(serializer.errors, safe=False)
        except Exception as e:
            return JsonResponse(str(e), safe=False)


class getEmployeeFamilyData(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            Userdata = User.objects.filter(username=request.user).values()[0]
            id = Userdata["id"]
            employee_family_data = list(FamilyEmergencyContacts.objects.filter(empid=id).values())
            data = {
                'Message': "Employee Family Details",
                "data": employee_family_data
            }
            return JsonResponse(data, safe=False)
        except Exception as e:
            return JsonResponse(str(e), safe=False)


class postEmployeeBankData(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        try:
            serializer = postEmployeeBankDataSerializer(data=request.data)
            if serializer.is_valid():
                data = User.objects.filter(username=request.user).values()[0]
                id = data["id"]
                AccountType = serializer.data['AccountType']
                AccountName = serializer.data['AccountName']
                IFSCCode = serializer.data['IFSCCode']
                BankName = serializer.data['BankName']
                AccountNumber = serializer.data['AccountNumber']

                EmployeeBankDetails.objects.create(
                    empid_id = id,
                    AccountType=AccountType,
                    AccountName=AccountName,
                    IFSCCode=IFSCCode,
                    BankName=BankName,
                    AccountNumber=AccountNumber)
                data = {'Message': "Employee Bank Details Created Successfully"}
                return JsonResponse(data, safe=False)
            return JsonResponse(serializer.errors, safe=False)
        except Exception as e:
            return JsonResponse(str(e), safe=False)

class getEmployeeBankData(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            Userdata = User.objects.filter(username=request.user).values()[0]
            id = Userdata["id"]

            result = list(EmployeeBankDetails.objects.filter(empid_id=id).values())
            print(result)
            data = {
            'Message': "Employee Details",
            "data": result
            }
            return JsonResponse(data, safe=False)
        except Exception as e:
            return JsonResponse(str(e), safe=False)


class updateEmployeeBankData(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            serializer = updateEmployeeBankDataSerializer(data=request.data)
            if serializer.is_valid():
                data = User.objects.filter(username=request.user).values()[0]
                id = data["id"]

                EmployeeBankDetails.objects.filter(empid_id=id).update(
                    **serializer.data
                )
                data = {'Message': "Employee Bank Details Updated Successfully"}
                return JsonResponse(data, safe=False)
            return JsonResponse(serializer.errors, safe=False)
        except Exception as e:
            return JsonResponse(str(e), safe=False)








