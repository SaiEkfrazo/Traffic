# Generated by Django 5.0.1 on 2024-01-07 12:51

import dashboard.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_traffic_date_alter_traffic_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='traffic',
            name='report',
            field=models.FileField(default=1, upload_to=dashboard.models.unique_report_path),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='traffic',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='traffic',
            name='time',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
