# Generated by Django 5.0 on 2023-12-30 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radio',
            name='Logo',
            field=models.FileField(upload_to='static/images'),
        ),
    ]
