# Generated by Django 5.0.4 on 2024-04-23 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_foodhubuser_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodhubuser',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='foodhubuser',
            name='is_superadmin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='foodhubuser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]