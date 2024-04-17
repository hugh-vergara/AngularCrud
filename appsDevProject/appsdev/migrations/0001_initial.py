# Generated by Django 5.0.2 on 2024-04-03 22:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('collid', models.IntegerField(primary_key=True, serialize=False)),
                ('collfullname', models.CharField(max_length=100)),
                ('collshortname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('deptid', models.IntegerField(primary_key=True, serialize=False)),
                ('deptfullname', models.CharField(max_length=100)),
                ('deptshortname', models.CharField(blank=True, max_length=20, null=True)),
                ('deptcollid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appsdev.college')),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('progid', models.IntegerField(primary_key=True, serialize=False)),
                ('progfullname', models.CharField(max_length=100)),
                ('progshortname', models.CharField(blank=True, max_length=20, null=True)),
                ('progcolldeptid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appsdev.department')),
                ('progcollid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appsdev.college')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studid', models.IntegerField(primary_key=True, serialize=False)),
                ('studfirstname', models.CharField(max_length=50)),
                ('studlastname', models.CharField(max_length=50)),
                ('studmidname', models.CharField(blank=True, max_length=50, null=True)),
                ('studyear', models.IntegerField()),
                ('studcollid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appsdev.college')),
                ('studprogid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appsdev.program')),
            ],
        ),
    ]
