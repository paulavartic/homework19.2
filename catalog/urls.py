from django.urls import path
from catalog.apps import NewappConfig
from catalog.views import products_list, contacts
app_name = NewappConfig.name

urlpatterns = [
    path('', products_list, name='home'),
    path('contacts/', contacts, name='contacts')
]
