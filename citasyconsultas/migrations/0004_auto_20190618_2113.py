# Generated by Django 2.2.1 on 2019-06-19 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citasyconsultas', '0003_auto_20190618_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='fecCon',
            field=models.DateField(help_text='Seleccione la fecha para la cita'),
        ),
    ]
