from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from .serializers import *
from django.contrib.auth.models import User
from .models import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
import datetime

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
                    username = username

                )

                #EmployeeLeaveIntialization
                # EmployeeTotalLeaveData.objects.create(empid_id = id,leaveType="CasualLeave")
                # EmployeeTotalLeaveData.objects.create(empid_id=id, leaveType="SickLeave")
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
            print(employee_data)
            result = {}
            result["username"] = employee_data["username"]
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
                relationshipType = serializer.data["relationshipType"]
                relationshipName = serializer.data["relationshipName"]
                contactNumber = serializer.data['contactNumber']
                Address = serializer.data['Address']

                print("username=", request.user)
                data = User.objects.filter(username=request.user).values()[0]
                id = data["id"]

                FamilyEmergencyContacts.objects.create(
                    empid_id = id,
                    relationshipName=relationshipName,
                    relationshipType=relationshipType,
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
            print(type(employee_family_data))
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

                EmployeeBankDetails.objects.create(
                    empid_id = id,
                    **serializer.data
                )
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
            'Message': "Employee Bank Details",
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

                AccountNumber = serializer.data["AccountNumber"]
                EmployeeBankDetails.objects.filter(empid_id=id,AccountNumber=AccountNumber).update(
                    **serializer.data
                )
                data = {'Message': "Employee Bank Details Updated Successfully"}
                return JsonResponse(data, safe=False)
            return JsonResponse(serializer.errors, safe=False)
        except Exception as e:
            return JsonResponse(str(e), safe=False)


class postEmployeeLeaveAllocation(APIView):
    def post(self, request):
        try:
            serializer = postEmployeeLeaveAllocationSerializer(data=request.data)
            if serializer.is_valid():
                username = serializer.data["username"]
                leaveType = serializer.data["leaveType"]
                leaveCount = serializer.data["leaveCount"]

                if User.objects.filter(username=username).exists():
                    data = User.objects.filter(username=username).values()[0]
                    id = data["id"]

                    EmployeeLeaveData.objects.create(
                        empid_id=id,
                        leaveType=leaveType,
                        leaveCount=leaveCount,
                    )

                    leaveCountData = EmployeeTotalLeaveData.objects.filter(empid_id=id,leaveType = leaveType).values()[0]
                    NewLeaveCount = int(leaveCountData["TotalleaveCount"]) + int(leaveCount)
                    print(NewLeaveCount)

                    EmployeeTotalLeaveData.objects.filter(empid_id=id).update(TotalleaveCount=NewLeaveCount)
                    data = {'Message': "Employee Leave Updated Successfully"}
                    return JsonResponse(data, safe=False)

                else:
                    return JsonResponse({
                        "status": 400,
                        "message": "User Not Exist With Provided username",
                    })
            return JsonResponse(serializer.errors, safe=False)
        except Exception as e:
            return JsonResponse(str(e), safe=False,status=status.HTTP_400_BAD_REQUEST)


class getEmployeeLeaveData(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            Userdata = User.objects.filter(username=request.user).values()[0]
            id = Userdata["id"]

            result = list(EmployeeLeaveData.objects.filter(empid_id=id).values())
            print(result)
            data = {
                'Message': "Employee Details Leave Data",
                "data": result
            }
            return JsonResponse(data, safe=False)
        except Exception as e:
            return JsonResponse(str(e), safe=False)

class EmployeeLandingPage(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        try:
            username = request.user
            userData = str(username) + "!"
            menu = ["PROFILE","ATTENDANCE AND LEAVE MANAGEMENT",
                    "HR HELPDESK","PAYROLL MANAGEMENT","APPRAISAL"
                    "ANNOUNCEMENT","SKILL AND PROJECT MANAGEMENT"]

            currentTime = datetime.datetime.now()
            if currentTime.hour < 12:
                greeting='Good Morning.'
            elif 12 <= currentTime.hour < 16:
                greeting='Good Afternoon.'
            else:
                greeting='Good Evening.'
            result = {
                    "message": userData,
                    "menu" : menu,
                    "greetings": greeting
                    }
            return JsonResponse(result, safe=False,status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse(str(e), safe=False, status=status.HTTP_400_BAD_REQUEST)


class EmployeeProfileMenu(APIView):
    def post(self,request):
        try:
            serializer = EmployeeProfileMenuSerializer(data=request.data)
            if serializer.is_valid():
                menu = serializer.data["menu"]
                submenu = ["EMPLOYEE IDENTIFICATION", "FAMILY AND EMERGENCY CONTACT",
                        "QUALIFICATION DETAILS", "WORK EXPERIENCE", "LANGUAGE DETAILS"
                                                             "ROLE", "MY PHOTO","BANK DETAILS","PASSPORT DETAILS","PROJECT DETAILS","ORGANISATION CHART"]
                result ={
                "menu": menu,
                "submenu":submenu
                }
                return JsonResponse(result, safe=False, status=status.HTTP_200_OK)
            return JsonResponse(serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse(str(e), safe=False, status=status.HTTP_400_BAD_REQUEST)


class updateEmployeeFamilyData(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        try:
            serializer = updateEmployeeFamilyDataSerialzer(data=request.data)
            if serializer.is_valid():
                print("username=", request.user)
                data = User.objects.filter(username=request.user).values()[0]
                id = data["id"]
                relationshipId = serializer.data["relationshipId"]

                FamilyEmergencyContacts.objects.filter(empid_id=id,relationshipId=relationshipId).update(
                    **serializer.data
                )

                result ={
                "message" : "Family & Emergency Contacts Updated"
                }
                return JsonResponse(result, safe=False, status=status.HTTP_200_OK)
            return JsonResponse(serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse(str(e), safe=False, status=status.HTTP_400_BAD_REQUEST)


class postEmployeequalificationData(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            serializer = postEmployeequalificationDataSerializer(data=request.data)
            if serializer.is_valid():
                data = User.objects.filter(username=request.user).values()[0]
                id = data["id"]

                print(data, type(data))
                Employeequalification.objects.create(
                    empid_id=id,
                    **serializer.data
                )
                data = {'Message': "Employee qualification details uploaded Successfully"}
                return JsonResponse(data, safe=False)
            return JsonResponse(serializer.errors, safe=False)
        except Exception as e:
            return JsonResponse(str(e), safe=False)

class getEmployeequalificationData(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            Userdata = User.objects.filter(username=request.user).values()[0]
            id = Userdata["id"]

            result = list(Employeequalification.objects.filter(empid=id).values())
            print(result)
            data = {
                'Message': "Qualification Details",
                "data": result
            }
            return JsonResponse(data, safe=False)
        except Exception as e:
            return JsonResponse(str(e), safe=False)

class postEmployeeworkData(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            serializer = postEmployeeworkDataSerializer(data=request.data)
            if serializer.is_valid():
                data = User.objects.filter(username=request.user).values()[0]
                id = data["id"]

                Workexperience.objects.create(
                    empid_id=id,
                    **serializer.data
                )
                data = {'Message': "Employee work experience Created Successfully"}
                return JsonResponse(data, safe=False)
            return JsonResponse(serializer.errors, safe=False)
        except Exception as e:
            return JsonResponse(str(e), safe=False)


class getEmployeeworkData(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            Userdata = User.objects.filter(username=request.user).values()[0]
            id = Userdata["id"]

            result = list(Workexperience.objects.filter(empid_id=id).values())
            print(result)
            data = {
                'Message': "Employee Work Experience Details",
                "data": result
            }
            return JsonResponse(data, safe=False)
        except Exception as e:
            return JsonResponse(str(e), safe=False)


class postEmployeelanguageData(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            serializer = postEmployeelanguageSerializer(data=request.data)
            if serializer.is_valid():
                data = User.objects.filter(username=request.user).values()[0]
                id = data["id"]

                EmployeeLanguage.objects.create(
                    empid_id=id,
                    **serializer.data,
                )
                data = {'Message': "Employee language Created Successfully"}
                return JsonResponse(data, safe=False)
            return JsonResponse(serializer.errors, safe=False)
        except Exception as e:
            return JsonResponse(str(e), safe=False)


class getEmployeelanguageData(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            Userdata = User.objects.filter(username=request.user).values()[0]
            id = Userdata["id"]

            result = list(EmployeeLanguage.objects.filter(empid_id=id).values())
            print(result)
            data = {
                'Message': "Employee language Details",
                "data": result
            }
            return JsonResponse(data, safe=False)
        except Exception as e:
            return JsonResponse(str(e), safe=False)


class postEmployeeRoleData(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            serializer = postEmployeeRoleDataSerializer(data=request.data)
            if serializer.is_valid():
                data = User.objects.filter(username=request.user).values()[0]
                id = data["id"]
                EmployeeRole.objects.filter(empid=id).update(status=False)
                EmployeeRole.objects.create(
                    empid_id=id,
                    **serializer.data
                )

                data = {'Message': "Employee Role Created Successfully"}
                return JsonResponse(data, safe=False)
            return JsonResponse(serializer.errors, safe=False)
        except Exception as e:
            return JsonResponse(str(e), safe=False)


class getEmployeeRoleData(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            Userdata = User.objects.filter(username=request.user).values()[0]
            id = Userdata["id"]

            result = EmployeeRole.objects.filter(empid_id=id,status=True).values()[0]
            print(result)
            data = {
                'Message': "Employee Role Details",
                "data": result
            }
            return JsonResponse(data, safe=False)
        except Exception as e:
            return JsonResponse(str(e), safe=False)


class postEmployeeProjectData(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        try:
            serializer = postEmployeeprojectSerializer(data=request.data)
            if serializer.is_valid():
                data = User.objects.filter(username=request.user).values()[0]
                id = data["id"]
                projectManager = serializer.data["projectManager"]
                if User.objects.filter(username=projectManager).exists():
                    EmployeeProjectDetails.objects.create(
                        empid_id=id,
                        **serializer.data)
                    data = {'Message': "Employee project Details Created Successfully"}
                    return JsonResponse(data, safe=False,status=status.HTTP_200_OK)
                else:
                    data = {'Message': "Employee Manager Not Exists"}
                    return JsonResponse(data, safe=False,status= status.HTTP_400_BAD_REQUEST)

            return JsonResponse(serializer.errors, safe=False)
        except Exception as e:
            return JsonResponse(str(e), safe=False)


class getEmployeeProjectData(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            Userdata = User.objects.filter(username=request.user).values()[0]
            id = Userdata["id"]

            result = list(EmployeeProjectDetails.objects.filter(empid_id=id).values())
            print(result)
            data = {
                'Message': "Employee Project Details",
                "data": result
            }
            return JsonResponse(data, safe=False)
        except Exception as e:
            return JsonResponse(str(e), safe=False)