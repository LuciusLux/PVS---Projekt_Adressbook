# Generated by Django 3.2 on 2021-05-03 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_contact', '0002_auto_20210503_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='type',
            field=models.CharField(choices=[('RES', 'private'), ('SME', 'business')], max_length=3),
        ),
    ]
