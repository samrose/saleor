from __future__ import unicode_literals

from django.http import HttpResponsePermanentRedirect
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.utils.translation import ugettext as _

from .forms import get_form_class_for_product
from .models import Product, Category
from saleor.cart import Cart


def get_related_products(product):
    if not product.collection:
        return []
    related_products = Product.objects.filter(
        collection=product.collection)
    related_products = related_products.prefetch_related('images')
    return related_products


def product_details(request, slug, product_id):
    product = get_object_or_404(Product.objects.select_subclasses(),
                                id=product_id)
    if product.get_slug() != slug:
        return HttpResponsePermanentRedirect(product.get_absolute_url())
    form_class = get_form_class_for_product(product)
    cart = Cart.for_session_cart(request.cart, discounts=request.discounts)
    form = form_class(cart=cart, product=product,
                      data=request.POST or None)
    if form.is_valid():
        if form.cleaned_data['quantity']:
            msg = _('Added %(product)s to your cart.') % {
                'product': product}
            messages.success(request, msg)
        form.save()
        return redirect('product:details', slug=slug, product_id=product_id)
    template_name = 'product/details_%s.html' % (
        type(product).__name__.lower(),)
    templates = [template_name, 'product/details.html']
    related_products = get_related_products(product)
    return TemplateResponse(
        request, templates,
        {'product': product, 'form': form,
         'related_products': related_products})


def category_index(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all().select_subclasses()
    products = products.prefetch_related('images')
    return TemplateResponse(
        request, 'category/index.html',
        {'products': products, 'category': category})
