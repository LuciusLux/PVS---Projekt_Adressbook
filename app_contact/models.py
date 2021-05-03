from django.db import models

# Create your models here.
# Contact Model
class Contact(models.Model):
    CONTACT_TYPES = (
        ('priv', 'private'),
        ('busi', 'business'),
    )
    name = models.CharField(max_length=256)
    first_name = models.CharField(max_length=256)
    type = models.CharField(max_length=4, choices=CONTACT_TYPES)

    addresses = models.ManyToManyField('Address', related_name='contacts')


# Address Model
class Address(models.Model):
    street = models.CharField(max_length=256)
    zip = models.CharField(max_length=10)
    city = models.CharField(max_length=256)
    country = models.CharField(max_length=2)