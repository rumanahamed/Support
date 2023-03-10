# Generated by Django 4.0.2 on 2022-08-31 09:57

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Workexperience',
            fields=[
                ('workId', models.AutoField(primary_key=True, serialize=False)),
                ('companyName', models.CharField(max_length=100)),
                ('Location', models.CharField(max_length=100)),
                ('Role', models.CharField(choices=[('Management', 'Management'), ('Frontend', 'Frontend'), ('Backend', 'Backend'), ('Testing', 'Testing')], max_length=100)),
                ('YearOfExperience', models.FloatField()),
                ('empid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SkillManagement',
            fields=[
                ('SkillId', models.AutoField(primary_key=True, serialize=False)),
                ('SkillName', models.CharField(max_length=100)),
                ('ProficientLevel', models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], max_length=100)),
                ('Experience', models.FloatField()),
                ('LastUsed', models.CharField(max_length=100)),
                ('empid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FamilyEmergencyContacts',
            fields=[
                ('relationshipId', models.AutoField(primary_key=True, serialize=False)),
                ('relationshipName', models.CharField(max_length=100)),
                ('relationshipType', models.CharField(max_length=100)),
                ('contactNumber', models.IntegerField(unique=True)),
                ('Address', models.CharField(max_length=100)),
                ('empid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeVisaAndPermit',
            fields=[
                ('VisaRecordId', models.AutoField(primary_key=True, serialize=False)),
                ('CountryName', models.CharField(max_length=10)),
                ('Citizen', models.BooleanField(default=False)),
                ('permitType', models.CharField(max_length=100)),
                ('DateOfIssue', models.DateField()),
                ('DateOfExpire', models.DateField()),
                ('empid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeTotalLeaveData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leaveType', models.CharField(blank=True, choices=[('CasualLeave', 'CasualLeave'), ('SickLeave', 'SickLeave'), ('PrevilageLeave', 'PrevilageLeave')], max_length=100, null=True)),
                ('TotalleaveCount', models.IntegerField(default=0)),
                ('datetime', models.DateTimeField(default=datetime.datetime(2022, 8, 31, 15, 27, 2, 901532))),
                ('empid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeTicket',
            fields=[
                ('ticketId', models.AutoField(primary_key=True, serialize=False)),
                ('ticketDescription', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('HR', 'HR'), ('IT', 'IT'), ('Salary', 'Salary'), ('Other', 'Other'), ('Admin', 'Admin')], max_length=100)),
                ('attachment', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(choices=[('Unassigned Tickets', 'Unassigned Tickets'), ('Open Tickets', 'Open Tickets'), ('Solved Tickets', 'Solved Tickets')], default='Unassigned Tickets', max_length=100)),
                ('assigne', models.CharField(default='a649116', max_length=100)),
                ('empid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeRole',
            fields=[
                ('Role', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True)),
                ('empid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employeequalification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QualificationType', models.CharField(choices=[('Intermediate', 'Intermediate'), ('Graduation', 'Graduation'), ('Post Graduation', 'Post Graduation')], max_length=100)),
                ('Board', models.CharField(max_length=100)),
                ('Year_of_passing', models.CharField(max_length=4)),
                ('certificate_no', models.CharField(max_length=100, unique=True)),
                ('Institute', models.CharField(max_length=100)),
                ('Location', models.CharField(max_length=100)),
                ('Percentage', models.FloatField()),
                ('empid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeProjectDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectName', models.CharField(max_length=100)),
                ('clientName', models.CharField(max_length=100)),
                ('duration', models.FloatField()),
                ('status', models.BooleanField()),
                ('projectStartDate', models.DateField()),
                ('projectManager', models.CharField(max_length=100)),
                ('technology', models.TextField()),
                ('empid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeePayroll',
            fields=[
                ('salarySlip', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('taxSheet', models.CharField(max_length=100, unique=True)),
                ('month', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('empid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeePassport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PassportNumber', models.CharField(max_length=100, unique=True)),
                ('PlaceOfIssue', models.CharField(max_length=100)),
                ('DateOfIssue', models.DateField()),
                ('DateOfExpire', models.DateField()),
                ('empid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=100, unique=True)),
                ('speak', models.CharField(choices=[('HIGH', 'HIGH'), ('MEDIUM', 'MEDIUM'), ('LOW', 'LOW')], max_length=100)),
                ('read', models.CharField(choices=[('HIGH', 'HIGH'), ('MEDIUM', 'MEDIUM'), ('LOW', 'LOW')], max_length=100)),
                ('write', models.CharField(choices=[('HIGH', 'HIGH'), ('MEDIUM', 'MEDIUM'), ('LOW', 'LOW')], max_length=100)),
                ('empid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeCreditLeaveData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leaveType', models.CharField(choices=[('CasualLeave', 'CasualLeave'), ('SickLeave', 'SickLeave'), ('PrevilageLeave', 'PrevilageLeave')], max_length=100)),
                ('leaveCount', models.IntegerField()),
                ('datetime', models.DateTimeField(default=datetime.datetime(2022, 8, 31, 15, 27, 2, 901532))),
                ('month', models.CharField(max_length=100)),
                ('empid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeBankDetails',
            fields=[
                ('AccountType', models.CharField(choices=[('Salary Account', 'Salary Account'), ('PPF Account', 'PPF Account')], max_length=100)),
                ('AccountName', models.CharField(max_length=100)),
                ('IFSCCode', models.CharField(max_length=100)),
                ('BankName', models.CharField(max_length=100)),
                ('AccountNumber', models.IntegerField(primary_key=True, serialize=False)),
                ('empid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeApplyLeave',
            fields=[
                ('leaveId', models.AutoField(primary_key=True, serialize=False)),
                ('leaveType', models.CharField(choices=[('CasualLeave', 'CasualLeave'), ('SickLeave', 'SickLeave'), ('PrevilageLeave', 'PrevilageLeave')], max_length=100)),
                ('leaveDescription', models.CharField(max_length=100)),
                ('leaveStatus', models.CharField(choices=[('Approved', 'Approved'), ('Pending', 'Pending'), ('Canceled', 'Canceled')], default='Pending', max_length=100)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='uploads')),
                ('assigne', models.CharField(max_length=100)),
                ('from_date', models.DateField(blank=True, null=True)),
                ('to_date', models.DateField(blank=True, null=True)),
                ('leaveCount', models.FloatField(default=0)),
                ('empid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeAnnouncement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.CharField(blank=True, max_length=100, null=True)),
                ('Date', models.DateTimeField(default=datetime.datetime(2022, 8, 31, 15, 27, 2, 902531))),
                ('Announcement', models.TextField()),
                ('empid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('password', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Photo', models.CharField(blank=True, max_length=100, null=True)),
                ('Mobile', models.IntegerField(blank=True, null=True)),
                ('OfficePhone', models.IntegerField(blank=True, null=True)),
                ('HomeAddress', models.CharField(blank=True, max_length=100, null=True)),
                ('WorkAddress', models.CharField(blank=True, max_length=100, null=True)),
                ('AdharCard', models.CharField(blank=True, max_length=100, null=True)),
                ('Pancard', models.CharField(blank=True, max_length=100, null=True)),
                ('Passport', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('WorkEmail', models.CharField(blank=True, max_length=100, null=True)),
                ('Designation', models.CharField(blank=True, max_length=100, null=True)),
                ('AboutMe', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('JoiningDate', models.DateTimeField(blank=True, null=True)),
                ('CreatedDate', models.DateTimeField(blank=True, null=True)),
                ('FirstName', models.CharField(blank=True, max_length=50, null=True)),
                ('lastName', models.CharField(blank=True, max_length=50, null=True)),
                ('Location', models.CharField(blank=True, max_length=100, null=True)),
                ('DOB', models.DateTimeField(blank=True, null=True)),
                ('Gender', models.CharField(blank=True, max_length=100, null=True)),
                ('ManagerId', models.CharField(default='a649116', max_length=100)),
                ('level', models.IntegerField()),
                ('empid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
