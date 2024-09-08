# Generated by Django 5.0.7 on 2024-09-08 18:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_alter_product_price"),
    ]

    operations = [
        migrations.CreateModel(
            name="Version",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "version_number",
                    models.PositiveIntegerField(
                        help_text="Fill in the version number",
                        verbose_name="Version number",
                    ),
                ),
                (
                    "version_name",
                    models.CharField(
                        help_text="Fill in the name",
                        max_length=150,
                        verbose_name="Version name",
                    ),
                ),
                (
                    "current_version",
                    models.BooleanField(
                        default=False, verbose_name="Current version indicator"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="version",
                        to="catalog.product",
                        verbose_name="Product name",
                    ),
                ),
            ],
            options={
                "verbose_name": "Version",
                "verbose_name_plural": "Versions",
            },
        ),
    ]
