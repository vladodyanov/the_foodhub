# Generated by Django 5.0.4 on 2024-05-09 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_foodhubuser_is_admin_foodhubuser_is_superadmin_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='address_line_1',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='address_line_2',
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
