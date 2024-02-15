# Generated by Django 5.0.1 on 2024-01-27 17:50

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=256)),
                ('answer', models.CharField(max_length=4000)),
            ],
        ),
        migrations.CreateModel(
            name='PageContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('summary', models.CharField(max_length=1000)),
                ('category', models.CharField(max_length=256)),
                ('content1Title', models.CharField(max_length=256)),
                ('content1Description', models.CharField(max_length=1000)),
                ('content2Title', models.CharField(max_length=256)),
                ('content2Description', models.CharField(max_length=1000)),
                ('content3Title', models.CharField(max_length=256)),
                ('content3Description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('date_of_birth', models.DateField()),
                ('mobile', models.CharField(blank=True, max_length=50, null=True)),
                ('date_created', models.DateField(default=datetime.date.today)),
                ('user_type', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='pagecontent',
            constraint=models.UniqueConstraint(fields=('category',), name='unique_category'),
        ),
    ]
