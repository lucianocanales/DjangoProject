# Generated by Django 3.1.3 on 2021-01-29 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0009_auto_20210128_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='caracteristica',
            field=models.ManyToManyField(to='tienda.Caracteristica'),
        ),
    ]
