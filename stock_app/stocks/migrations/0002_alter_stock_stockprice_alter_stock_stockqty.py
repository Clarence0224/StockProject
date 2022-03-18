# Generated by Django 4.0.3 on 2022-03-18 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='stockprice',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='stock',
            name='stockqty',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]