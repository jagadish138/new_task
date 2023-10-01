# Generated by Django 4.2.5 on 2023-09-30 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_deg', models.CharField(max_length=100)),
                ('emp_salary', models.IntegerField()),
                ('emp_join_date', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=100)),
                ('emp_age', models.IntegerField()),
                ('emp_email', models.CharField(max_length=100)),
                ('emp_number', models.CharField(max_length=100)),
                ('emp_address', models.CharField(max_length=100)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.role')),
            ],
        ),
    ]
