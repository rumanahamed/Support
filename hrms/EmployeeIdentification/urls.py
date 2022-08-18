from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/EmployeeOnboard/',views.EmployeeOnboardRegister.as_view()), #HR
    path('api/login/',obtain_auth_token),
    path('api/updateEmployeeData/',views.updateEmployeeData.as_view()),
    path('api/getEmployeeData/',views.getEmployeeData.as_view()),
    path('api/postEmployeeFamilyData/',views.postEmployeeFamilyData.as_view()),
    path('api/getEmployeeFamilyData/',views.getEmployeeFamilyData.as_view()),
    path('api/postEmployeeBankData/',views.postEmployeeBankData.as_view()),
    path('api/getEmployeeBankData/',views.getEmployeeBankData.as_view()),
    path('api/updateEmployeeBankData/',views.updateEmployeeBankData.as_view()),
]