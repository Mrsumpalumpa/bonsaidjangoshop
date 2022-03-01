from django.contrib import admin
from .models import product,contact

class productadmin(admin.ModelAdmin):
    list_display= ("productname","productsection")
    search_fields=("productname","productstock","productprice")
    list_filter=("productname","productsection")

class contactadmin(admin.ModelAdmin):
    list_display= ("contactname","contactemail")
    search_fields=("contactname","contactemail","contactissuetype")
    list_filter=("contactissuetype",)


# Register your models here.
admin.site.register(product,productadmin)
admin.site.register(contact,contactadmin)
