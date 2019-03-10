from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name="list"),
    path('category/(?P<hierarchy>.+)/', views.show_category, name='category'),
]
