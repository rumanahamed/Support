import ast

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
from pathlib import Path
from rest_framework.response import Response

class EmployeeOnboardRegister(APIView):
    def post(self,request):
        try:
            serializer = EmployeeOnboardSerializer(data= request.data)
            if serializer.is_valid():
                username = serializer.data['username']
                email = serializer.data['email']
                password = serializer.data["password"]
                level= serializer.data["level"]
                ManagerId= serializer.data["ManagerId"]

                User.objects.create_user(username=username, password=password,email=email)
                data = User.objects.filter(username=username).values()[0]
                id = data["id"]

                Employee.objects.create(
                    empid_id = id,
                    password = password,
                    username = username,
                    level=level,
                    ManagerId=ManagerId

                )

                #EmployeeLeaveIntialization
                EmployeeTotalLeaveData.objects.create(empid_id = id,leaveType="CasualLeave")
                EmployeeTotalLeaveData.objects.create(empid_id=id, leaveType="SickLeave")
                EmployeeTotalLeaveData.objects.create(empid_id=id, leaveType="PrevilageLeave")

                #EmployeeBlankSalaryData
                EmployeeBankDetails.objects.create(empid_id=id,AccountType="SalaryAccount")
                EmployeeBankDetails.objects.create(empid_id=id, AccountType="PPFAccount")

                #EmployeeBlankPassportData
                EmployeePassport.objects.create(empid_id=id)
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
            result["FirstName"] = employee_data["FirstName"]

            data = {
                    'Message': "Employee Details",
                    "data": result
                    }
            return JsonResponse(data, safe=False)
        except Exception as e:
            return JsonResponse(str(e), safe=False)

class getEmployeeDataName(APIView):
    def get(self, request, ):
            try:
                data2 = Employee.objects.filter().values()
                # print(data2)
                result = []
                for var in data2:
                    result.append(var["username"])

                return Response({
                    'status': 200,
                    'data': result
                })

            except Exception as e:
                return Response({
                    'status': 400,
                    'message': 'Something went wrong',
                    'errors': str(e)
                })


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


class getEmployeeParticularFamilyData(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request,relationshipId):
        try:
            Userdata = User.objects.filter(username=request.user).values()[0]
            id = Userdata["id"]
            employee_family_data = list(FamilyEmergencyContacts.objects.filter(empid=id,relationshipId=relationshipId).values())
            data = {
                'Message': "Employee Family Relationship Data",
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


class getEmployeeSalaryBankData(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request,AccountType):
        try:
            Userdata = User.objects.filter(username=request.user).values()[0]
            id = Userdata["id"]

            result = list(EmployeeBankDetails.objects.filter(empid_id=id,AccountType=AccountType).values())
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
                AccountType=serializer.data["AccountType"]
                AccountName=serializer.data["AccountName"]
                IFSCCode = serializer.data["IFSCCode"]
                BankName = serializer.data["BankName"]
                EmployeeBankDetails.objects.filter(
                    empid_id=id,AccountType=AccountType).update(
                    AccountNumber=AccountNumber,
                    AccountName=AccountName,
                    IFSCCode=IFSCCode,
                    BankName=BankName
                )
                data = {'Message': "Employee Bank Details Updated Successfully"}
                return JsonResponse(data, safe=False)
            return JsonResponse(serializer.errors, safe=False)
        except Exception as e:
            return JsonResponse(str(e), safe=False)


class postEmployeeLeaveCredit(APIView):
    def post(self, request):
        try:
            serializer = postEmployeeLeaveCreditSerializer(data=request.data)
            if serializer.is_valid():
                username = serializer.data["username"]
                leaveType = serializer.data["leaveType"]
                leaveCount = serializer.data["leaveCount"]
                month = serializer.data["month"]
                if User.objects.filter(username=username).exists():
                    data = User.objects.filter(username=username).values()[0]
                    id = data["id"]

                    EmployeeCreditLeaveData.objects.create(
                        empid_id=id,
                        leaveType=leaveType,
                        leaveCount=leaveCount,
                        month= month
                    )

                    leaveCountData = EmployeeTotalLeaveData.objects.filter(empid_id=id,leaveType = leaveType).values()[0]
                    NewLeaveCount = int(leaveCountData["TotalleaveCount"]) + int(leaveCount)
                    print(NewLeaveCount)

                    EmployeeTotalLeaveData.objects.filter(empid_id=id,leaveType = leaveType).update(TotalleaveCount=NewLeaveCount)
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


class getEmployeeLeaveCreditDetails(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request,leavetype):
        try:
            Userdata = User.objects.filter(username=request.user).values()[0]
            id = Userdata["id"]

            leaveDetails = list(EmployeeCreditLeaveData.objects.filter(
                empid_id=id,
                leaveType=leavetype
            ).values())
            print(leaveDetails)
            data = {
                'Message': "Employee Details Leave Data",
                "data": leaveDetails
            }
            return JsonResponse(data, safe=False)
        except Exception as e:
            return JsonResponse(str(e), safe=False)

class getEmployeeLeaveall(APIView):
    def get(self, request,):
        try:

            leaveDetails = list(EmployeeApplyLeave.objects.filter().values())
            print(leaveDetails)
            data = {
                'Message': "Employee Details Leave Data",
                "data": leaveDetails
            }
            return JsonResponse(data, safe=False)
        except Exception as e:
            return JsonResponse(str(e), safe=False)

class getEmployeeLeaveData(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            Userdata = User.objects.filter(username=request.user).values()[0]
            id = Userdata["id"]

            result = list(EmployeeTotalLeaveData.objects.filter(empid_id=id).values())
            print(result)
            data = {
                'Message': "Employee Details Leave Data",
                "data": result
            }
            return JsonResponse(data, safe=False)
        except Exception as e:
            return JsonResponse(str(e), safe=False)


class postEmployeeLeaveApply(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        try:
            serializer = postEmployeeLeaveApplyserializer(data=request.data)
            if serializer.is_valid():
                Userdata = User.objects.filter(username=request.user).values()[0]
                id = Userdata["id"]
                leaveType = serializer.data["leaveType"]
                leaveDescription= serializer.data["leaveDescription"]
                assigne= id  #Manger_id
                date_format = "%Y-%m-%d"
                from_date=serializer.data["from_date"]
                to_date=serializer.data["to_date"]
                print(from_date,type(from_date))
                a = datetime.datetime.strptime(from_date, date_format)
                print(a,type(a))
                b = datetime.datetime.strptime(to_date, date_format)
                leaveCount = (b - a).days
                print(leaveCount,type(leaveCount))
                print(leaveType)

                AvialableLeaveCount = EmployeeTotalLeaveData.objects.filter(leaveType=leaveType,empid_id=id).values()[0]["TotalleaveCount"]
                print("AvialableLeaveCount===",AvialableLeaveCount)
                if int(leaveCount) <= int(AvialableLeaveCount):
                    EmployeeApplyLeave.objects.create(
                        empid_id = id,
                        leaveType=leaveType,
                        assigne=assigne,
                        from_date=from_date,
                        to_date=to_date,
                        leaveCount=leaveCount
                    )
                    data={"Message":"Leave Applied Successfully"}
                    return JsonResponse(data, safe=False,status=status.HTTP_200_OK)
                else:
                    data = {"Message": "Not Sufficient leave to Apply"}
                    return JsonResponse(data, safe=False, status=status.HTTP_200_OK)

            return JsonResponse(serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse(str(e), safe=False,status=status.HTTP_400_BAD_REQUEST)


class getManagerLeaveDashboard(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        try:
            Userdata = User.objects.filter(username=request.user).values()[0]
            id = Userdata["id"]

            LeaveData = list(EmployeeApplyLeave.objects.filter(assigne=id).values())

            data={
                    "Message": "Leave List Data",
                    "DATA": LeaveData
                }
            return JsonResponse(data, safe=False, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse(str(e), safe=False, status=status.HTTP_400_BAD_REQUEST)


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


class updateEmployeequlificationData(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        try:
            serializer = updateEmployeequlificationDataSerialzer(data=request.data)
            if serializer.is_valid():
                print("username=", request.user)
                data = User.objects.filter(username=request.user).values()[0]
                id = data["id"]
                qualificationId = serializer.data["id"]

                Employeequalification.objects.filter(empid_id=id,id=qualificationId).update(
                    **serializer.data
                )

                result ={
                "message" : "Employee Qualification Updated Updated"
                }
                return JsonResponse(result, safe=False, status=status.HTTP_200_OK)
            return JsonResponse(serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse(str(e), safe=False, status=status.HTTP_400_BAD_REQUEST)


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


class updateEmployeelanguageData(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        try:
            serializer = updateEmployeelanguageDataSerialzer(data=request.data)
            if serializer.is_valid():
                print("username=", request.user)
                data = User.objects.filter(username=request.user).values()[0]
                id = data["id"]
                languageID = serializer.data["id"]

                EmployeeLanguage.objects.filter(empid_id=id,id=languageID).update(
                    **serializer.data
                )

                result ={
                "message" : "Employee Language Updated Successfully"
                }
                return JsonResponse(result, safe=False, status=status.HTTP_200_OK)
            return JsonResponse(serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse(str(e), safe=False, status=status.HTTP_400_BAD_REQUEST)

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


class getEmployeeLeaveDashboard(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            Userdata = User.objects.filter(username=request.user).values()[0]
            id = Userdata["id"]

            result = list(EmployeeApplyLeave.objects.filter(empid_id=id).values())
            print(result)
            approvedCount=0
            PendingCount=0
            CanceledCount=0
            TotalLeaveCount=0

            for var in result:
                if var["leaveStatus"] == "Pending":
                    PendingCount=PendingCount+1
                elif var["leaveStatus"] == "Canceled":
                    CanceledCount=CanceledCount+1
                elif var["leaveStatus"] == "Approved":
                    approvedCount=approvedCount+1
            leaveAllocatedData = list(EmployeeTotalLeaveData.objects.filter(empid_id=id).values())
            print("leaveAllocatedData==",leaveAllocatedData)
            for var in leaveAllocatedData:
                midLeave = var["TotalleaveCount"]
                TotalLeaveCount+=midLeave
            dataLeave = {"Approved": approvedCount, "Pending": PendingCount, "Canceled": CanceledCount,"TotalLeaveCount":TotalLeaveCount}
            return JsonResponse(dataLeave, safe=False)
        except Exception as e:
            return JsonResponse(str(e), safe=False)

class getEmployeeTotalLeaveCount(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request,leaveStatus):
        try:
            Userdata = User.objects.filter(username=request.user).values()[0]
            id = Userdata["id"]

            result = list(EmployeeApplyLeave.objects.filter(empid_id=id,leaveStatus=leaveStatus).values())
            print(result)
            dataLeave = {"result": result}
            return JsonResponse(dataLeave, safe=False)
        except Exception as e:
            return JsonResponse(str(e), safe=False)


class postEmployeeLeaveApprove(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        try:
            serializer = postEmployeeLeaveApproveserializer(data=request.data)
            if serializer.is_valid():
                Userdata = User.objects.filter(username=request.user).values()[0]
                id = Userdata["id"]

                empid = serializer.data["empid"]
                leaveId = serializer.data["leaveId"]
                statusData = serializer.data["statusData"]

                EmployeeApplyLeave.objects.filter(empid=empid,leaveId=leaveId,assigne=id).update(leaveStatus=statusData)

                data={"Message": "Leave Updated Successfully"}
                return JsonResponse(data, safe=False, status=status.HTTP_200_OK)
            return JsonResponse(serializer.errors, safe=False,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse(str(e), safe=False,status=status.HTTP_400_BAD_REQUEST)




class postEmployeeTicketCreate(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        try:
            serializer = postEmployeeTicketCreateserializer(data=request.data)
            if serializer.is_valid():
                Userdata = User.objects.filter(username=request.user).values()[0]
                id = Userdata["id"]

                EmployeeTicket.objects.create(
                    empid_id=id,
                    **serializer.data
                )
                data = {"Message": "Ticket Created Successfully"}
                return JsonResponse(data, safe=False, status=status.HTTP_200_OK)
            return JsonResponse(serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse(str(e), safe=False, status=status.HTTP_400_BAD_REQUEST)


class getEmployeeTicketDashboard(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            Userdata = User.objects.filter(username=request.user).values()[0]
            id = Userdata["id"]

            result = list(EmployeeTicket.objects.filter(empid_id=id).values())
            print(result)
            UnassignedTickets = 0
            OpenTickets = 0
            SolvedTickets = 0

            for var in result:
                if var["status"] == "UnassignedTickets":
                    UnassignedTickets = UnassignedTickets + 1
                elif var["status"] == "OpenTickets":
                    OpenTickets = OpenTickets + 1
                elif var["status"] == "SolvedTickets":
                    SolvedTickets = SolvedTickets + 1

            dataLeave = {"SolvedTickets": SolvedTickets, "OpenTickets": OpenTickets, "UnassignedTickets": UnassignedTickets}
            return JsonResponse(dataLeave, safe=False,status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse(str(e), safe=False,status=status.HTTP_400_BAD_REQUEST)

class getEmployeeTicketDetails(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request,ticketstatus):
        try:
            Userdata = User.objects.filter(username=request.user).values()[0]
            id = Userdata["id"]

            ticketDetails = list(EmployeeTicket.objects.filter(
                empid_id=id,
                status=ticketstatus
            ).values())
            print(ticketDetails)
            data = {
                'Message': "Employee Ticket Details",
                "data": ticketDetails
            }
            return JsonResponse(data, safe=False)
        except Exception as e:
            return JsonResponse(str(e), safe=False)

class getEmployeeTicketHistory(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request,):
        try:
            Userdata = User.objects.filter(username=request.user).values()[0]
            id = Userdata["id"]

            ticketDetails = list(EmployeeTicket.objects.filter(
                empid_id=id
            ).values())
            print(ticketDetails)
            data = {
                'Message': "Employee Ticket History Details",
                "data": ticketDetails
            }
            return JsonResponse(data, safe=False)
        except Exception as e:
            return JsonResponse(str(e), safe=False)

class postEmployeeAnnouncement(APIView):

    def post(self, request):
        try:
            serializer = postEmployeeAnnouncementSerializer(data=request.data)
            if serializer.is_valid():
                empid = serializer.data['empid']
                data = User.objects.filter(username=empid).values()[0]
                id = data["id"]

                Announcement = serializer.data['Announcement']

                EmployeeAnnouncement.objects.create(
                    empid_id=id,
                    Announcement=Announcement
                )
                data = {'Message': "Employee Announcement Published"}
                return JsonResponse(data, safe=False,status=status.HTTP_200_OK)

            return JsonResponse(serializer.errors, safe=False,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse(str(e), safe=False)


class getEmployeeAnnouncement(APIView):

    def get(self, request):
        try:
            result = EmployeeAnnouncement.objects.all()
            print(result)
            result2 = getEmployeeAnnouncementSeralizer(result,many=True)
            data = {
                'Message': "Employee Announcement",
                "data": result2.data
            }
            return JsonResponse(data, safe=False,status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse(str(e), safe=False,status=status.HTTP_400_BAD_REQUEST)


class getEmployeeAnnouncementUsername(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            Userdata = User.objects.filter(username=request.user).values()[0]
            id = Userdata["id"]
            employee_data = Employee.objects.filter(empid=id).values()[0]
            print(employee_data)
            result = {}
            result["username"] = employee_data["username"]

            data = {
                'Message': "Announcement Username",
                "data": result
            }
            return JsonResponse(data, safe=False)
        except Exception as e:
            return JsonResponse(str(e), safe=False)




class postEmployeeSkillManagement(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
            try:
                serializer = postEmployeeSkillManagementSerializer(data=request.data)
                if serializer.is_valid():
                    data = User.objects.filter(username=request.user).values()[0]
                    id = data["id"]

                    SkillManagement.objects.create(
                        empid_id=id,
                        **serializer.data
                    )
                    data = {'Message': "Employee skill created  Successfully"}
                    return JsonResponse(data, safe=False, status=status.HTTP_200_OK)
                return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return JsonResponse(str(e), safe=False,status=status.HTTP_400_BAD_REQUEST)


class getEmployeeSkillManagement(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            Userdata = User.objects.filter(username=request.user).values()[0]
            id = Userdata["id"]

            result = list(SkillManagement.objects.filter(empid_id=id).values())
            print(result)
            data = {
                'Message': "Employee Skill Details",
                "data": result
            }
            return JsonResponse(data, safe=False,status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse(str(e), safe=False,status=status.HTTP_400_BAD_REQUEST)

class getEmployeeSkillType(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request,ProficientLevel):
        try:
            Userdata = User.objects.filter(username=request.user).values()[0]
            id = Userdata["id"]

            result = list(SkillManagement.objects.filter(empid_id=id,ProficientLevel=ProficientLevel).values())
            print(result)
            data = {
                'Message': "Employee Skill Details",
                "data": result
            }
            return JsonResponse(data, safe=False,status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse(str(e), safe=False,status=status.HTTP_400_BAD_REQUEST)


class getEmployeeSkillDashboard(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            Userdata = User.objects.filter(username=request.user).values()[0]
            id = Userdata["id"]

            result = list(SkillManagement.objects.filter(empid_id=id).values())
            print(result)
            SkillCount=0
            BeginnerCount = 0
            IntermediateCount = 0
            AdvancedCount =0


            for var in result:
                if "SkillName" in var.keys():
                    SkillCount = SkillCount + 1
                if var["ProficientLevel"] == "Beginner":
                        BeginnerCount = BeginnerCount + 1
                        print(BeginnerCount)
                elif var["ProficientLevel"] == "Intermediate":
                        IntermediateCount = IntermediateCount + 1
                elif var["ProficientLevel"] == "Advanced":
                        AdvancedCount = AdvancedCount + 1

            dataSkill = {"SkillCount":SkillCount,"Beginner":BeginnerCount, "Intermediate": IntermediateCount ,"Advanced":AdvancedCount}
            return JsonResponse(dataSkill, safe=False,status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse(str(e), safe=False,status=status.HTTP_400_BAD_REQUEST)


class postEmployeePayrollManagement(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            serializer = postEmployeePayrollManagementSerializer(data=request.data)
            if serializer.is_valid():
                data = User.objects.filter(username=request.user).values()[0]
                id = data["id"]

                EmployeePayroll.objects.create(
                    empid_id=id,
                    **serializer.data
                )
                data = {'Message': "Employee Payroll Uploaded  Successfully"}
                return JsonResponse(data, safe=False, status=status.HTTP_200_OK)
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse(str(e), safe=False, status=status.HTTP_400_BAD_REQUEST)



class getEmployeePayrollManagement(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            Userdata = User.objects.filter(username=request.user).values()[0]
            id = Userdata["id"]

            result = list(EmployeePayroll.objects.filter(empid_id=id).values())
            print(result)
            data = {
                'Message': "Employee Payroll Details",
                "data": result
            }
            return JsonResponse(data, safe=False, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse(str(e), safe=False, status=status.HTTP_400_BAD_REQUEST)

class updateEmployeeUploadImages(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            serializer = postEmployeeUploadImagesSerializer(data=request.data)
            if serializer.is_valid():
                data = User.objects.filter(username=request.user).values()[0]
                id = data["id"]
                Photo = serializer.data['Photo']

                Employee.objects.filter(empid_id=id).update(Photo=Photo)
                data = {'Message': "Employee  image upload Successfully"}
                return JsonResponse(data, safe=False, status=status.HTTP_200_OK)
            return JsonResponse(serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse(str(e), safe=False, status=status.HTTP_400_BAD_REQUEST)


class getEmployeeImages(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            Userdata = User.objects.filter(username=request.user).values()[0]
            id = Userdata["id"]
            finaldata = {}
            result = Employee.objects.filter(empid_id=id).values()[0]
            print(result)

            result2 = EmployeeRole.objects.filter(empid_id=id, status=True).values()[0]
            print(result2)

            ImageData = [result["Photo"]]
            finaldata["ImageData"] =ImageData
            finaldata["Role"] = result2["Role"]
            for var in ImageData:
                print(type(var))
                var2 = var.replace("\\","/")
                var3 = var2.replace("//", "/")
            print(var3)
            finaldata["ImageData"] = var3

            data = {
                'Message': "Employee  Image details",
                "data": finaldata
            }
            return JsonResponse(data, safe=False,status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse(str(e), safe=False,status=status.HTTP_400_BAD_REQUEST)


class UploadImage(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        try:
            data = request.data
            serializer = UploadImageSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                print(str(serializer.data))
                data = User.objects.filter(username=request.user).values()[0]
                id = data["id"]
                Photo = serializer.data["file"]
                print(Photo)
                current_dir_path = Path().absolute()
                print("current_dir_path/=",current_dir_path)
                data_path = str(current_dir_path)+"/" + Photo
                print(data_path)
                Employee.objects.filter(empid_id=id).update(Photo=data_path)
                return JsonResponse({
                        'status': 200,
                        'message': 'Image Upload Successfully',
                        'ImagePath': str(serializer.data)
                        })
        except Exception as e:
                return JsonResponse({
                    'status': 400,
                    'message': 'Image Upload Failed',
                    "error" : str(e)
            })


class postEmployeePassportData(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            serializer = postEmployeePassportDataSerializer(data=request.data)
            if serializer.is_valid():
                data = User.objects.filter(username=request.user).values()[0]
                id = data["id"]

                EmployeePassport.objects.filter(
                    empid_id=id,

                ).update(**serializer.data)
                data = {'Message': "Employee Passport detail Updated Successfully"}
                return JsonResponse(data, safe=False, status=status.HTTP_200_OK)

            return JsonResponse(serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse(str(e), safe=False, status=status.HTTP_400_BAD_REQUEST)


class getEmployeePassportData(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            Userdata = User.objects.filter(username=request.user).values()[0]
            id = Userdata["id"]

            result = list(EmployeePassport.objects.filter(empid_id=id).values())
            print(result)
            data = {
                'Message': "Employee Passport Details",
                "data": result
            }
            return JsonResponse(data, safe=False,status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse(str(e), safe=False,status=status.HTTP_400_BAD_REQUEST)


class postEmployeeVisaAndPermitData(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            serializer = postEmployeeVisaAndPermitDataSerializer(data=request.data)
            if serializer.is_valid():
                data = User.objects.filter(username=request.user).values()[0]
                id = data["id"]

                EmployeeVisaAndPermit.objects.create(
                    empid_id=id,
                    **serializer.data
                )
                data = {'Message': "Employee Visa & Permit detail Created Successfully"}
                return JsonResponse(data, safe=False, status=status.HTTP_200_OK)

            return JsonResponse(serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse(str(e), safe=False, status=status.HTTP_400_BAD_REQUEST)

class updateEmployeeVisaAndPermitData(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            serializer = updateEmployeeVisaAndPermitDataSerializer(data=request.data)

            if serializer.is_valid():
                VisaRecordId = serializer.data["VisaRecordId"]
                CountryName = serializer.data["CountryName"]
                Citizen = serializer.data["Citizen"]
                permitType = serializer.data["permitType"]
                DateOfIssue = serializer.data["DateOfIssue"]
                DateOfExpire = serializer.data["DateOfExpire"]
                data = User.objects.filter(username=request.user).values()[0]
                id = data["id"]

                EmployeeVisaAndPermit.objects.filter(
                    empid_id=id,
                    VisaRecordId=VisaRecordId
                ).update(DateOfExpire=DateOfExpire,CountryName=CountryName,Citizen=Citizen,permitType=permitType,DateOfIssue=DateOfIssue)
                data = {'Message': "Employee Visa & Permit detail Updated Successfully"}
                return JsonResponse(data, safe=False, status=status.HTTP_200_OK)

            return JsonResponse(serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse(str(e), safe=False, status=status.HTTP_400_BAD_REQUEST)

class deleteEmployeeVisaAndPermitData(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            serializer = deleteEmployeeVisaAndPermitDataSerializer(data=request.data)

            if serializer.is_valid():
                VisaRecordId = serializer.data["VisaRecordId"]

                data = User.objects.filter(username=request.user).values()[0]
                id = data["id"]

                EmployeeVisaAndPermit.objects.filter(
                    empid_id=id,
                    VisaRecordId=VisaRecordId
                ).delete()
                data = {'Message': "Employee Visa & Permit detail Deleted Successfully"}
                return JsonResponse(data, safe=False, status=status.HTTP_200_OK)

            return JsonResponse(serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse(str(e), safe=False, status=status.HTTP_400_BAD_REQUEST)


class getEmployeeVisaAndPermitData(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            Userdata = User.objects.filter(username=request.user).values()[0]
            id = Userdata["id"]

            result = list(EmployeeVisaAndPermit.objects.filter(empid_id=id).values())
            print(result)
            data = {
                'Message': "Employee Visa & Permit Details",
                "data": result
            }
            return JsonResponse(data, safe=False, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse(str(e), safe=False, status=status.HTTP_400_BAD_REQUEST)


class getEmployeeOrganisationChart(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            Userdata = User.objects.filter(username=request.user).values()[0]
            id = Userdata["id"]
            organisationchart = []
            result = Employee.objects.filter(empid =id).values()[0]
            print(result)
            result2 = EmployeeRole.objects.filter(empid_id=id).values()[0]
            print(result2)
            level_result = result["level"]
            role_result = result2["Role"]


            higherEmployeeData = list(Employee.objects.filter(level__lt=level_result).values())
            higherEmployeeIDList = [var["username"] for var in higherEmployeeData ]
            higherEmployeeRole = list(EmployeeRole.objects.filter(Role=role_result).values())
            higherEmployeeRole = [var["Role"] for var in higherEmployeeRole]
            lowerEmployeeData = list(Employee.objects.filter(level__gt=level_result).values())
            lowerEmployeeIDList = [var["username"] for var in lowerEmployeeData]
            equalEmployeeData = list(Employee.objects.filter(Q(level=level_result)))
            equalEmployeeIDList=[]
            for var in equalEmployeeData:
                equalEmployeeIDList.append(str(var))
            data = {
                'Message': "Employee Organisation Chart",
                "Employee Level": level_result,
                "Employee":result["username"],
                "Role": higherEmployeeRole[0],
                "higherEmployeeIDList": higherEmployeeIDList,
                "lowerEmployeeIDList" : lowerEmployeeIDList,
                "equalEmployeeIDList" : ast.literal_eval(str(equalEmployeeIDList))
            }
            return JsonResponse(data, safe=False, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse(str(e), safe=False, status=status.HTTP_400_BAD_REQUEST)


class userLogout(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            print(request.user)
            request.user.auth_token.delete()

            return JsonResponse({
                        'status': 200,
                        'message': 'Logout Successfully'
                    })

        except Exception as e:
            return JsonResponse({
                'status': 400,
                'message': 'Something went Wrong',
            })


class getEmployeeOrganisation(APIView):

    def get(self, request,username):
        try:
            Userdata = User.objects.filter(username=username).values()[0]
            id = Userdata["id"]
            organisationchart = []
            result = Employee.objects.filter(empid_id=id).values()[0]
            print(result)
            result2 = EmployeeRole.objects.filter(empid_id=id).values()[0]
            print(result2)
            level_result = result["level"]
            role_result = result2["Role"]
            higherEmployeeData = list(Employee.objects.filter(level__lt=level_result).values())
            higherEmployeeIDList = [var["username"] for var in higherEmployeeData ]
            higherEmployeeRole = list(EmployeeRole.objects.filter(Role=role_result).values())
            higherEmployeeRole = [var["Role"] for var in higherEmployeeRole]
            lowerEmployeeData = list(Employee.objects.filter(level__gt=level_result).values())
            lowerEmployeeIDList = [var["username"] for var in lowerEmployeeData]
            equalEmployeeData = list(Employee.objects.filter(Q(level=level_result)))
            equalEmployeeIDList=[]
            for var in equalEmployeeData:
                equalEmployeeIDList.append(str(var))
            data = {
                'Message': "Employee Organisation Chart",
                "Employee Level": level_result,
                "Employee":result["username"],
                "Role": higherEmployeeRole[0],
                "higherEmployeeIDList": higherEmployeeIDList,
                "lowerEmployeeIDList" : lowerEmployeeIDList,
                "equalEmployeeIDList" : ast.literal_eval(str(equalEmployeeIDList))
            }
            return JsonResponse(data, safe=False, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse(str(e), safe=False, status=status.HTTP_400_BAD_REQUEST)

