# Generated by Django 2.2.1 on 2019-06-20 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postres', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postres',
            name='img',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='postres',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='postres',
            name='precio',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='postres',
            name='stock',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterModelTable(
            name='postres',
            table='postres',
        ),
    ]
