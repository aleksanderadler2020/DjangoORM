from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    sort_type = request.GET.get('st')
    if sort_type is None or sort_type == 'name':
        phones = Phone.objects.order_by('name')
    elif sort_type == 'cheap':
        phones = Phone.objects.order_by('price')
    elif sort_type == 'expensive':
        phones = Phone.objects.order_by('-price')
    else:
        phones = Phone.objects.all()

    template = 'catalog.html'
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)






