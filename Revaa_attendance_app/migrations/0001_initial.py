# Generated by Django 4.2.2 on 2023-08-11 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeDetails',
            fields=[
                ('Name', models.CharField(max_length=20)),
                ('Age', models.IntegerField()),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=20)),
                ('Date_of_birth', models.DateField()),
                ('Father_name', models.CharField(max_length=20)),
                ('Number', models.CharField(max_length=10)),
                ('Emergency_no', models.CharField(help_text='Father number or Guardian number', max_length=10)),
                ('Official_email', models.CharField(max_length=20)),
                ('Address', models.TextField(max_length=50)),
                ('Blood_group', models.CharField(choices=[('A+', 'A+'), ('A1+', 'A1+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('A1B-', 'A1B-'), ('O+', 'O+'), ('O-', 'O-')], max_length=5)),
                ('Employee_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Employee_role', models.CharField(max_length=20)),
                ('date_of_join', models.DateField()),
                ('Password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('intime', models.TimeField()),
                ('Lunch', models.TimeField()),
                ('AfterLunch', models.TimeField()),
                ('Break', models.TimeField()),
                ('AfterL_Break', models.TimeField()),
                ('Leave', models.TimeField()),
                ('Outtime', models.TimeField()),
                ('Emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Revaa_attendance_app.employeedetails')),
            ],
        ),
    ]
