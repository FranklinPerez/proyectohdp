# Generated by Django 2.2.1 on 2019-06-22 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citasyconsultas', '0020_auto_20190622_0918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consulta',
            name='estCon',
        ),
        migrations.AddField(
            model_name='consulta',
            name='estado',
            field=models.CharField(blank=True, choices=[('f', 'Finalizar'), ('p', 'Pendiente')], default='p', max_length=1),
        ),
    ]
