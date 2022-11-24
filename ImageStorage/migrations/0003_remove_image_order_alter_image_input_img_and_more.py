# Generated by Django 4.1.3 on 2022-11-24 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ImageStorage', '0002_remove_image_type_remove_image_url_image_input_img_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='order',
        ),
        migrations.AlterField(
            model_name='image',
            name='input_img',
            field=models.FileField(blank=True, null=True, upload_to='input/', verbose_name='입력사진'),
        ),
        migrations.AlterField(
            model_name='image',
            name='output_img',
            field=models.FileField(blank=True, null=True, upload_to='output/', verbose_name='결과사진'),
        ),
    ]
