# Generated by Django 5.0.7 on 2024-08-14 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_product_manufactured_at_alter_category_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
