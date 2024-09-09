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
        upload_to="catalog/photo",
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
        related_name="catalog",
    )
    price = models.IntegerField(blank=True, null=True)
    created_at = models.DateField(blank=True, null=True, verbose_name="Creation date")
    updated_at = models.DateField(
        blank=True, null=True, verbose_name="Date of the last update"
    )
    manufactured_at = models.DateField(blank=True, null=True, verbose_name="Product manufactured at")

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["name", "category"]

    def __str__(self):
        return self.name


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        verbose_name='Product name',
        related_name='version',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    version_number = models.PositiveIntegerField(
        verbose_name='Version number',
        help_text='Fill in the version number',
    )
    version_name = models.CharField(
        verbose_name='Version name',
        help_text='Fill in the name',
        max_length=150,
    )
    current_version = models.BooleanField(
        verbose_name='Current version indicator',
        default=True,
    )

    class Meta:
        verbose_name = 'Version'
        verbose_name_plural = 'Versions'

    def __str__(self):
        return self.version_name

