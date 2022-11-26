# Generated by Django 4.1.3 on 2022-11-26 06:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter',
            name='bookmark',
            field=models.ManyToManyField(blank=True, related_name='bookmark_filter', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='filter',
            name='filter_image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]