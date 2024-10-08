from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField
from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'photo', 'category', 'price',)

    class ProductModeratorForm(StyleFormMixin, ModelForm):
        class Meta:
            model = Product
            fields = ('description', 'category', 'is_published')

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        for i in ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']:
            if i in cleaned_data.lower():
                raise ValidationError('You have used a forbidden word')
        return cleaned_data


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = ('product', 'version_name', 'version_number', 'current_version')


class ProductModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ('description', 'category')
