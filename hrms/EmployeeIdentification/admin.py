from django.contrib import admin
from .models import *

admin.site.register(Employee)
admin.site.register(FamilyEmergencyContacts)
admin.site.register(EmployeeBankDetails)
admin.site.register(EmployeeApplyLeave)
admin.site.register(EmployeeCreditLeaveData)
admin.site.register(EmployeeTotalLeaveData)
admin.site.register(Employeequalification)
admin.site.register(EmployeeLanguage)
admin.site.register(EmployeeRole)

