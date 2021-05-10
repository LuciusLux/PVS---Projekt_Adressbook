from django.contrib import admin
from .models import Contact, Address

# Register your models here.

class AdressInline(admin.StackedInline):
    model = Address
    extra = 0
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['__str__','type']
    list_filter = ['type']
    search_fields = ['name', 'first_name']
    inlines = [AddressInline]


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass