# Generated by Django 5.1.1 on 2024-09-30 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_singup_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singup',
            name='username',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]
