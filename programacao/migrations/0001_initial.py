# Generated by Django 5.0 on 2023-12-29 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Programacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_programacao', models.CharField(max_length=100)),
                ('horario', models.TimeField()),
                ('loucutor', models.CharField(max_length=100)),
                ('detalhes', models.TextField(null=True)),
                ('turno', models.CharField(max_length=50)),
            ],
        ),
    ]
