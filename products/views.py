from django.shortcuts import render
from products.models import Product

# Create your views here.
def get_product(request, slug):
    try:
        product = Product.objects.get(slug=slug)
        context = {'product': product}

        if request.GET.get('storage'):
            storage = request.GET.get('storage')
            print(storage)

            total_price = product.get_product_price_by_storage(storage)
            print(total_price)
            context['selected_storage'] = storage
            context['total_price'] = total_price


        return render(request, 'product/product.html', context=context)

    except Exception as e:
        print(e)
