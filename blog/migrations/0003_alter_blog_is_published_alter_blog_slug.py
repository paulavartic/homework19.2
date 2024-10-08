# Generated by Django 5.0.7 on 2024-08-30 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_blog_created_at_alter_blog_views_count"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="is_published",
            field=models.BooleanField(default=True, verbose_name="Published"),
        ),
        migrations.AlterField(
            model_name="blog",
            name="slug",
            field=models.CharField(
                blank=True, max_length=150, null=True, verbose_name="Slug"
            ),
        ),
    ]
