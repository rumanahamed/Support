# Generated by Django 4.0.2 on 2022-08-28 12:05

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('EmployeeIdentification', '0010_alter_employeelanguage_language_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeleavedata',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 28, 17, 35, 44, 593678)),
        ),
        migrations.AlterField(
            model_name='employeetotalleavedata',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 28, 17, 35, 44, 593678)),
        ),
        migrations.CreateModel(
            name='EmployeeRole',
            fields=[
                ('Role', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True)),
                ('empid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
