# Generated by Django 5.0.1 on 2024-03-08 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homecareapp', '0008_appuser_user_type_provideruser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceprovider',
            name='details',
            field=models.TextField(blank=True, max_length=4000, null=True),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='summary',
            field=models.TextField(max_length=2000),
        ),
    ]
