from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/EmployeeOnboard/',views.EmployeeOnboardRegister.as_view()), #HR
    path('api/login/',obtain_auth_token),
    path('api/logout/',views.userLogout.as_view()),
    path('api/EmployeeLandingPage/',views.EmployeeLandingPage.as_view()),
    path('api/EmployeeProfileMenu/',views.EmployeeProfileMenu.as_view()),
    path('api/updateEmployeeData/',views.updateEmployeeData.as_view()),
    path('api/getEmployeeData/',views.getEmployeeData.as_view()),
    path('api/postEmployeeFamilyData/',views.postEmployeeFamilyData.as_view()),
    path('api/getEmployeeParticularFamilyData/<relationshipId>/',views.getEmployeeParticularFamilyData.as_view()),
    path('api/getEmployeeFamilyData/',views.getEmployeeFamilyData.as_view()),
    path('api/updateEmployeeFamilyData/',views.updateEmployeeFamilyData.as_view()),
    path('api/postEmployeeUploadImages/',views.postEmployeeUploadImages.as_view()),
    path('api/updateEmployeeUploadImages/',views.updateEmployeeUploadImages.as_view()),
    path('api/getEmployeeImages/',views.getEmployeeImages.as_view()),
    path('api/postEmployeePassportData/',views.postEmployeePassportData.as_view()),
    path('api/getEmployeePassportData/', views.getEmployeePassportData.as_view()),
    path('api/postEmployeeVisaAndPermitData/',views.postEmployeeVisaAndPermitData.as_view()),
    path('api/getEmployeeVisaAndPermitData/', views.getEmployeeVisaAndPermitData.as_view()),


    ####QualiFicationDetails#####
    path('api/postEmployeequlificationData/',views.postEmployeequalificationData.as_view()),
    path('api/getEmployeequlificationData/', views.getEmployeequalificationData.as_view()),
    path('api/updateEmployeequlificationData/', views.updateEmployeequlificationData.as_view()),

    ####WorkExperience#########
    path('api/postEmployeeworkData/',views.postEmployeeworkData.as_view()),
    path('api/getEmployeeworkData/', views.getEmployeeworkData.as_view()),

    #######language###############
    path('api/postEmployeelanguageData/', views.postEmployeelanguageData.as_view()),
    path('api/getEmployeelanguageData/', views.getEmployeelanguageData.as_view()),

    #####role############
    path('api/postEmployeeRoleData/', views.postEmployeeRoleData.as_view()),
    path('api/getEmployeeRoleData/', views.getEmployeeRoleData.as_view()),

    #####bankDetails#######
    path('api/postEmployeeBankData/',views.postEmployeeBankData.as_view()),
    path('api/getEmployeeBankData/',views.getEmployeeBankData.as_view()),

    ########project Details##########
    path('api/postEmployeeProjectData/', views.postEmployeeProjectData.as_view()),
    path('api/getEmployeeProjectData/', views.getEmployeeProjectData.as_view()),

    #######leave#####################
    path('api/postEmployeeLeaveCredit/',views.postEmployeeLeaveCredit.as_view()),
    path('api/getEmployeeLeaveData/',views.getEmployeeLeaveData.as_view()),
    path('api/postEmployeeLeaveApply/',views.postEmployeeLeaveApply.as_view()),
    path('api/getManagerLeaveDashboard/',views.getManagerLeaveDashboard.as_view()),
    path('api/getEmployeeLeaveDashboard/',views.getEmployeeLeaveDashboard.as_view()),
    path('api/postEmployeeLeaveApprove/',views.postEmployeeLeaveApprove.as_view()),

    #########ticket############
    path('api/postEmployeeTicketCreate/',views.postEmployeeTicketCreate.as_view()),
    path('api/getEmployeeTicketDashboard/',views.getEmployeeTicketDashboard.as_view()),

    ########Announcement###########
    path('api/postEmployeeAnnouncement/', views.postEmployeeAnnouncement.as_view()),
    path('api/getEmployeeAnnouncement/', views.getEmployeeAnnouncement.as_view()),

    ########SkillManagment###########
    path('api/postEmployeeSkillManagement/', views.postEmployeeSkillManagement.as_view()),
    path('api/getEmployeeSkillManagement/', views.getEmployeeSkillManagement.as_view()),
    path('api/getEmployeeSkillDashboard/', views.getEmployeeSkillDashboard.as_view()),

    #########payroll########################
    path('api/postEmployeePayrollManagement/', views.postEmployeePayrollManagement.as_view()),
    path('api/getEmployeePayrollManagement/', views.getEmployeePayrollManagement.as_view()),

    ###########EmployeeOrganisationChart##########
    path('api/getEmployeeOrganisationChart/', views.getEmployeeOrganisationChart.as_view()),
]