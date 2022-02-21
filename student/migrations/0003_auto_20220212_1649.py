# Generated by Django 3.2.8 on 2022-02-12 16:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0002_alter_studentprofile_adviser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='StudentDocuments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_letter', models.ImageField(upload_to='academic_records/')),
                ('jamb_original_result', models.ImageField(upload_to='academic_records/')),
                ('ssce_1', models.ImageField(upload_to='academic_records/')),
                ('ssce_2', models.ImageField(upload_to='academic_records/')),
                ('jamb_adm_letter', models.ImageField(upload_to='academic_records/')),
                ('state_of_origin', models.ImageField(upload_to='academic_records/')),
                ('birth_cert', models.ImageField(upload_to='academic_records/')),
                ('course_reg_100', models.ImageField(blank=True, null=True, upload_to='academic_records/')),
                ('payment_slip_100', models.ImageField(blank=True, null=True, upload_to='academic_records/')),
                ('course_reg_200', models.ImageField(blank=True, null=True, upload_to='academic_records/')),
                ('payment_slip_200', models.ImageField(blank=True, null=True, upload_to='academic_records/')),
                ('course_reg_300', models.ImageField(blank=True, null=True, upload_to='academic_records/')),
                ('payment_slip_300', models.ImageField(blank=True, null=True, upload_to='academic_records/')),
                ('course_reg_400', models.ImageField(blank=True, null=True, upload_to='academic_records/')),
                ('payment_slip_400', models.ImageField(blank=True, null=True, upload_to='academic_records/')),
                ('course_reg_500', models.ImageField(blank=True, null=True, upload_to='academic_records/')),
                ('payment_slip_500', models.ImageField(blank=True, null=True, upload_to='academic_records/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_document', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]