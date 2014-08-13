from django import forms
from django.utils.translation import pgettext_lazy
from selectable.forms import AutoCompleteWidget

from ..cart.forms import AddToCartForm
from .models import ServerForm
from .lookups import CollectionLookup


class ServerForm(AddToCartForm):

    #def get_variant(self, clean_data):
        #return self.product.variants.get(product__color=self.product.color)



class ImageInline(ProductVariantInline):
    error_no_items = pgettext_lazy('Product admin error', 'You have to add at least one image')


def get_form_class_for_product(product):
    if isinstance(product, Server):
        return ServerForm
    raise NotImplementedError
