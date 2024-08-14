from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Category name",
        help_text="Name category",
    )
    description = models.TextField(verbose_name="Description", help_text="Fill in description", blank=True, null=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Product name", help_text="Name product"
    )
    description = models.TextField(
        verbose_name="Product description", help_text="Describe product", blank=True, null=True
    )
    photo = models.ImageField(
        upload_to="products/photo",
        blank=True,
        null=True,
        verbose_name="Photo",
        help_text="Add photo",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Category name",
        null=True,
        blank=True,
        related_name="products",
    )
    price = models.IntegerField()
    created_at = models.DateField(blank=True, null=True, verbose_name="Creation date")
    updated_at = models.DateField(
        blank=True, null=True, verbose_name="Date of the last update"
    )

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["name", "category"]

    def __str__(self):
        return self.name


