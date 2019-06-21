# Generated by Django 2.2.1 on 2019-06-21 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citasyconsultas', '0006_auto_20190619_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='cita',
            name='servic',
            field=models.ManyToManyField(to='citasyconsultas.Servicio'),
        ),
        migrations.AlterField(
            model_name='cita',
            name='horCon',
            field=models.CharField(help_text='Seleccione un horario disponible', max_length=10, null=True),
        ),
    ]