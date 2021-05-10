from django.db import models

# Create your models here.
# Contact Model
class Contact(models.Model):
    CONTACT_TYPES = (
        ('RES', 'private'),
        ('SME', 'business'),
    )
    name = models.CharField(max_length=256)
    first_name = models.CharField(max_length=256)
    type = models.CharField(max_length=3, choices=CONTACT_TYPES, default='RES')

    def __str__(self):
        if 'RES' in self.type:
            return '%s %s' % (self.first_name, self.name)
        return self.name


# Address Model
class Address(models.Model):
    street = models.CharField(max_length=256)
    zip = models.CharField(max_length=10)
    city = models.CharField(max_length=256)
    country = models.CharField(max_length=2)

    def __str__(self):
        return '%s, %s %s' % (self.street, self.zip, self.city)

    contact = models.ForeignKey('Contact', on_delete=models.CASCADE, related_name='addresses')