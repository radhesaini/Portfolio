# Generated by Django 5.1.4 on 2025-01-03 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_project_created_at_project_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='image/'),
        ),
    ]