# Generated by Django 3.2.3 on 2021-06-08 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='idRegistro',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='id_registro'),
        ),
    ]
