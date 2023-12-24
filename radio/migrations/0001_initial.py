# Generated by Django 5.0 on 2023-12-24 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Radio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=255)),
                ('Frequencia', models.CharField(max_length=20)),
                ('Logo', models.FileField(upload_to='./media/images')),
                ('Link', models.CharField(max_length=255)),
            ],
        ),
    ]
