# Generated by Django 5.0.1 on 2024-01-07 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traffic',
            name='date',
            field=models.CharField(max_length=100),
        ),
    ]
