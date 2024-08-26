from django.urls import path
from catalog.apps import NewappConfig
from catalog.views import ProductListView, contacts, ProductDetailView
app_name = NewappConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_details')
]
