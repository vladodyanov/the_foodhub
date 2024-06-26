# Generated by Django 5.0.4 on 2024-04-22 08:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_foodhubuser_managers'),
        ('vendor', '0002_alter_vendor_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='user_profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to='accounts.profile'),
        ),
    ]
