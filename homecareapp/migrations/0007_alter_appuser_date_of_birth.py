# Generated by Django 5.0.1 on 2024-03-08 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homecareapp', '0006_remove_appuser_user_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='date_of_birth',
            field=models.CharField(max_length=256),
        ),
    ]