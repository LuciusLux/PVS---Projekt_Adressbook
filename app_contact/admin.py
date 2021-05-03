from django.contrib import admin
from .models import Contact, Address

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','type']
    list_filter = ['type']
    search_fields = ['name', 'first_name']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass