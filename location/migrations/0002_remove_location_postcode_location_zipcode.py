# Generated by Django 4.2.1 on 2023-05-24 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='postcode',
        ),
        migrations.AddField(
            model_name='location',
            name='zipcode',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]