#!/usr/bin/env python

from django import forms
from .models import Add

class DataForm(forms.Form):
    fruit_name = forms.CharField(max_length=30)
    fruit_price = forms.IntegerField()


class AddForm(forms.ModelForm):

    class Meta:
        model = Add
        fields = ('fruit_name', 'fruit_price')
