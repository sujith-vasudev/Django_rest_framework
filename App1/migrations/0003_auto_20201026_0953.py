# Generated by Django 3.0.7 on 2020-10-26 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0002_auto_20201026_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=200),
        ),
    ]
