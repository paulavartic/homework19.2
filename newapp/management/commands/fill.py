from django.core.management import BaseCommand
import json
from catalog.models import Product, Category


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('~/py_project/homework19.2/catalog_data.json', 'r', encoding='utf-8') as file:
            categories = json.load(file)
        return categories

    @staticmethod
    def json_read_products():
        with open('~/py_project/homework19.2/catalog_data.json', 'r', encoding='utf-8') as file:
            products = json.load(file)
        return products

    def handle(self, *args, **options):

        Product.objects.all().delete()
        Category.objects.all().delete()

        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(
                Category(
                    name=category['fields']['name'],
                    description=category['fields']['description'],
                )
            )

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(
                Product(
                    name=product['fields']['name'],
                    description=product['fields']['description'],
                    photo=product['fields']['photo'],
                    category=Category.objects.get(pk=category['pk']),
                    created_at=product['fields']['created_at'],
                    upadated_at=product['fields']['updated_at'],
                    manufactured_at=product['fields']['manufactured_at'],
                )
            )

        Product.objects.bulk_create(product_for_create)
