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



