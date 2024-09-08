from django.urls import path
from catalog.apps import NewappConfig
from catalog.views import ProductListView, contacts, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = NewappConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('create', ProductCreateView.as_view(), name='product_create'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='product_edit'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_details')
]
