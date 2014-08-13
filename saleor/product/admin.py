from django.contrib import admin

from mptt.admin import MPTTModelAdmin

from .models import (ProductImage, Server)
from .forms import ServerAdminForm, ImageInline


class ImageAdminInline(admin.StackedInline):
    model = ProductImage
    formset = ImageInline

class ServerAdmin(admin.ModelAdmin):
    form = ShirtAdminForm
    list_display = ['name', 'collection', 'admin_get_price_min',
                    'admin_get_price_max']
    inlines = [ImageAdminInline]


class ProductCollectionAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(Server, ServerAdmin)
admin.site.register(Category, MPTTModelAdmin)
admin.site.register(FixedProductDiscount)
