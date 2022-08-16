from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/EmployeeOnboard/',views.EmployeeOnboardRegister.as_view()), #HR
    path('api/login/',obtain_auth_token),
    path('api/updateEmployeeData/',views.updateEmployeeData.as_view())
]