# Generated by Django 2.2.1 on 2019-06-20 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citasyconsultas', '0005_auto_20190619_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secretaria',
            name='codSec',
            field=models.IntegerField(help_text='Ingrese el codigo de la Secretaria', primary_key=True, serialize=False),
        ),
    ]
