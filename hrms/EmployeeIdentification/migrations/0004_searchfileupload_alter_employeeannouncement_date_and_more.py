# Generated by Django 4.0.2 on 2022-12-06 12:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeIdentification', '0003_rename_years_employeeprojectdetails_duration_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='searchfileupload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='searchData/')),
            ],
        ),
        migrations.AlterField(
            model_name='employeeannouncement',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 6, 17, 31, 6, 461062)),
        ),
        migrations.AlterField(
            model_name='employeecreditleavedata',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 6, 17, 31, 6, 459060)),
        ),
        migrations.AlterField(
            model_name='employeeticket',
            name='status',
            field=models.CharField(choices=[('UnassignedTickets', 'UnassignedTickets'), ('OpenTickets', 'OpenTickets'), ('SolvedTickets', 'SolvedTickets')], default='UnassignedTickets', max_length=100),
        ),
        migrations.AlterField(
            model_name='employeetotalleavedata',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 6, 17, 31, 6, 460061)),
        ),
    ]
