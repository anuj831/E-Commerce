from django.contrib import admin
from .models import CustomUser, Category, Product

class ProductInline(admin.TabularInline):
    model = Product
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProductInline]

admin.site.register(CustomUser)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
admin.site.site_header = "Cirbrid Greenogy (I) Private Limited"
