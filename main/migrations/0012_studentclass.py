# Generated by Django 5.1.1 on 2024-10-01 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_singup_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentclass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(blank=True, max_length=70, null=True)),
                ('student', models.IntegerField()),
                ('subject', models.CharField(blank=True, max_length=70, null=True)),
                ('teacher', models.CharField(blank=True, max_length=70, null=True)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
    ]
