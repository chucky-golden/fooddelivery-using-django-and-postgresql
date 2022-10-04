from django.shortcuts import render, get_object_or_404
from .models import Dish
from .choices import price_choices
from django.core.paginator import Paginator


def index(request):
    dishes = Dish.objects.order_by('-dish_date').filter(is_published=True)
    paginator = Paginator(dishes, 1)
    page = request.GET.get('page')
    paged_dishes = paginator.get_page(page)

    context = {
        'dishes': paged_dishes
    }
    return render(request, 'dishes/dishes.html', context)


def dish(request, dish_id):
    dish = get_object_or_404(Dish, pk=dish_id)

    context = {
        'dish': dish
    }

    return render(request, 'dishes/dish.html', context)


def search(request):
    query_list = Dish.objects.order_by('-dish_date')

    # keyword
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        query_list = query_list.filter(name__icontains=keyword)

    # category
    if 'category' in request.GET:
        category = request.GET['category']
        query_list = query_list.filter(category__icontains=category)

    # price
    if 'price' in request.GET:
        price = request.GET['price']
        query_list = query_list.filter(price__lte=price)

    context = {
        'price_choices': price_choices,
        'dishes': query_list
    }

    return render(request, 'dishes/search.html', context)








