from django.forms import Form, ModelForm
from django.forms import CharField, BooleanField, ImageField
from django.forms import Textarea, CheckboxInput, HiddenInput

from .models import Universe


class PlaceForm(Form):
    name = CharField(max_length=40)
    description = CharField(widget=Textarea)
    is_public = BooleanField(widget=CheckboxInput, required=False, initial=True)
    thumbnail = ImageField()
    background = ImageField(required=False)


class WorldForm(Form):
    name = CharField(max_length=40)
    description = CharField(widget=Textarea)
    is_public = BooleanField(widget=CheckboxInput, required=False, initial=True)
    thumbnail = ImageField()
    background = ImageField(required=False)


class UniverseForm(ModelForm):
    class Meta:
        model = Universe
        fields = ['name', 'description', 'is_public', 'thumbnail', 'background']