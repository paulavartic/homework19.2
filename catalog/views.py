from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def products_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'products_list.html', context)


def contacts(request):
    return render(request,'contacts.html')


def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, 'product_details.html', context)


