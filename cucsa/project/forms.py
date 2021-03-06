from django import forms
from . import models
from item.models import Item
# from bootstrap_modal_forms.forms import BSModalForm


class ProjectForm(forms.ModelForm):

    class Meta:
        model = models.Project
        exclude = ['owner']

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        exclude = ['owner']