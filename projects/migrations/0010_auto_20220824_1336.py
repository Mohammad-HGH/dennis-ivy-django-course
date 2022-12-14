# Generated by Django 2.2.17 on 2022-08-24 09:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20220824_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='file',
            field=models.FileField(default=django.utils.timezone.now, upload_to='upload/', verbose_name='Document'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='upload/img'),
        ),
    ]
