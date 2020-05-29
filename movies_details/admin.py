from django.contrib import admin
from .forms import ProductModelForm
from .models import AddProduct 
# Register your models here.


class ProductModelAdmin(admin.ModelAdmin):
    #form = ProductModelForm
    class Meta:
        model = AddProduct
        
    
admin.site.register(AddProduct,ProductModelAdmin)

