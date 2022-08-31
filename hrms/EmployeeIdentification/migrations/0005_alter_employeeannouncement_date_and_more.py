# Generated by Django 4.0.2 on 2022-08-31 07:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('EmployeeIdentification', '0004_alter_employeeannouncement_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeannouncement',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 31, 12, 56, 35, 537200)),
        ),
        migrations.AlterField(
            model_name='employeecreditleavedata',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 31, 12, 56, 35, 536202)),
        ),
        migrations.AlterField(
            model_name='employeetotalleavedata',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 31, 12, 56, 35, 536202)),
        ),
        migrations.CreateModel(
            name='EmployeeVisaAndPermit',
            fields=[
                ('VisaRecordId', models.AutoField(primary_key=True, serialize=False)),
                ('CountryName', models.CharField(max_length=10)),
                ('Citizen', models.CharField(max_length=100)),
                ('permitType', models.CharField(max_length=100)),
                ('DateOfIssue', models.DateField()),
                ('DateOfExpire', models.DateField()),
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
    ]