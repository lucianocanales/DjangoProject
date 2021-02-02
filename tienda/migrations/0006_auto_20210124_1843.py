# Generated by Django 3.1.3 on 2021-01-24 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0005_auto_20210122_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caracteristica',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='imagecarousel',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='imagen',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='imagenproducto',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='caracteristica',
            field=models.ManyToManyField(to='tienda.Caracteristica'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
