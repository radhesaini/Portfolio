# Generated by Django 5.1.4 on 2025-01-03 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='../static/')),
                ('technologies', models.CharField(max_length=255)),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]