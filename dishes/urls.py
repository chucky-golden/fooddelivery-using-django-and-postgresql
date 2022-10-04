from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dishes'),
    path('<int:dish_id>', views.dish, name='dish'),
    path('search', views.search, name='search'),
]