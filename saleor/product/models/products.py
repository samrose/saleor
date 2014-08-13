from __future__ import unicode_literals

from django.utils.translation import pgettext_lazy
from django.db import models

from .base import Product
#from .variants import (ProductVariant, PhysicalProduct, ColoredVariant,
#                       StockedProduct)


class Server(Product):

    class Meta:
        app_label = 'product'
