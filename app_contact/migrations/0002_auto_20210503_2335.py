# Generated by Django 3.2 on 2021-05-03 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='addresses',
            field=models.ManyToManyField(related_name='contacts', to='app_contact.Address'),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='contact',
            name='type',
            field=models.CharField(choices=[('priv', 'private'), ('busi', 'business')], max_length=4),
        ),
    ]