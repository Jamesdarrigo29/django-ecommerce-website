from django.shortcuts import get_object_or_404, render

from .models import Product, Category


def product_all(request):
    products = Product.products.all()
    return render(request, 'store/index.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug,  in_stock=True)
    return render(request, 'store/single.html', {'product': product})


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/category.html', {'category': category, 'products': products})


def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        products = Product.objects.filter(name__contains=searched)
        return render(request, 'store/search-results.html', {'searched': searched, 'products': products})

    else:
        return render(request, 'store/search-results.html')
