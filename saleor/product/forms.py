from django import forms
from django.utils.translation import pgettext_lazy
from selectable.forms import AutoCompleteWidget

from ..cart.forms import AddToCartForm
from .models import Server
from .lookups import CollectionLookup


class ServerForm(AddToCartForm):

    def get_variant(self, clean_data):
        return self
class ServerAdminForm(forms.ModelForm):
    class Meta:
        model = Server
        widgets = {
                'collection': AutoCompleteWidget(CollectionLookup)
        }
class ProductVariantInline(forms.models.BaseInlineFormSet):
    error_no_items = pgettext_lazy('Product admin error', 'You have to create at least one variant')
    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data:
                count += 1
            if count < 1:
                raise forms.ValidationError(self.error_no_items)

class ImageInline(ProductVariantInline):
    error_no_items = pgettext_lazy('Product admin error', 'You have to add at least one image')


def get_form_class_for_product(product):
    if isinstance(product, Server):
        return ServerForm
    raise NotImplementedError
