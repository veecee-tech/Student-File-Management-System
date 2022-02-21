# Generated by Django 3.2.8 on 2022-02-10 12:24

import authentication.models
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
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('mat_no', models.CharField(blank=True, max_length=14, null=True)),
                ('student_id', models.CharField(blank=True, max_length=8, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('Female', 'Female')], max_length=10, null=True)),
                ('adviser', models.ForeignKey(default=authentication.models.Account, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='adviser', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
