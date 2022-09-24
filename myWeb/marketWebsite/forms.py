from django import forms
from django.forms import ModelForm
from django.utils import timezone
from .models import production


class ProductForm(ModelForm):
    class Meta:
        model = production
        fields = ('pimg', 'pname', 'ptype', 'pub_date',)