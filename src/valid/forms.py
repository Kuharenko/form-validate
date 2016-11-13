# -*- coding:utf-8 -*-
from django import forms
from valid.models import Car


class ProductForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["name", "description", "quality"]
        labels = {
            "name": 'Car',
            "description": 'About Car',
            "quality": 'Quality car',
        }
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form'}),
            "description": forms.Textarea()
        }

    def clean_quality(self):
        q = self.cleaned_data['quality']
        if int(q) < 0 or int(q) > 100:
            raise forms.ValidationError('Значение должно быть в пределах от 0-100')
        return q

    def clean_description(self):
        z = self.cleaned_data['description']
        if len(str(z)) < 10:
            raise forms.ValidationError('Длина описание должна быть больше 10 символов!')
        return z
