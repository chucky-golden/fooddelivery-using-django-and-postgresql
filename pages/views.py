from django.shortcuts import render
from dishes.models import Dish
from dishes.choices import price_choices


# Create your views here.
def index(request):
    dishes = Dish.objects.order_by('-dish_date').filter(is_published=True)[:3]
    
    context = {
        'price_choices': price_choices,
        'dishes': dishes
    }
    
    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')
