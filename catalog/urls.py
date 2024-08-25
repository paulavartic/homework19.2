from django.urls import path
from catalog.apps import NewappConfig
from catalog.views import products_list, contacts, product_details
app_name = NewappConfig.name

urlpatterns = [
    path('', products_list, name='products_list'),
    path('contacts/', contacts, name='contacts'),
    path('products/<int:pk>/', product_details, name='product_details' )
]
