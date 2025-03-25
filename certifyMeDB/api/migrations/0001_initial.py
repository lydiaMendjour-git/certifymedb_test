# Generated by Django 5.1.7 on 2025-03-25 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id_account', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('role', models.CharField(choices=[('université', 'Université'), ('entreprise', 'Entreprise'), ('ministère', 'Ministère'), ('école_privée', 'École Privée'), ('école_formation', 'École de Formation'), ('startup', 'Startup')], max_length=20)),
                ('is_verified', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, related_name='account_users', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='account_permissions', to='auth.permission')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
