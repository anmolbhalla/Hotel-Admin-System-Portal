# Generated by Django 2.0.3 on 2018-05-12 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_system', '0002_auto_20180512_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='date',
            field=models.DateField(),
        ),
    ]