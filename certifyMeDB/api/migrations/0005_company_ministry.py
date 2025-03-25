# Generated by Django 5.1.7 on 2025-03-25 20:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id_company', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=20)),
                ('id_account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='company', to='api.account')),
            ],
        ),
        migrations.CreateModel(
            name='Ministry',
            fields=[
                ('id_ministry', models.AutoField(primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=255)),
                ('id_account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ministry', to='api.account')),
            ],
        ),
    ]
