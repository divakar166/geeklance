# Generated by Django 4.1.12 on 2023-10-29 02:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='lancer',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('company', models.CharField(blank=True, max_length=200, null=True)),
                ('role', models.CharField(blank=True, max_length=100, null=True)),
                ('skills', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('bio', models.CharField(blank=True, max_length=100, null=True)),
                ('socials', models.CharField(max_length=100, null=True)),
                ('job_provided', models.CharField(max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('college', models.CharField(max_length=200)),
                ('role', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('job_completed', models.IntegerField(default=0)),
                ('earn', models.IntegerField(default=0)),
                ('ontime', models.IntegerField(default=0)),
                ('bio', models.CharField(blank=True, max_length=300)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('socials', models.CharField(blank=True, max_length=200, null=True)),
                ('pow', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
