from django.forms import Form, ModelForm
from django.forms import CharField, BooleanField, ImageField
from django.forms import Textarea, CheckboxInput, HiddenInput

from .models import Universe, World, Place


class PlaceForm(Form):
    name = CharField(max_length=40)
    description = CharField(widget=Textarea)
    is_public = BooleanField(widget=CheckboxInput, required=False, initial=True)
    thumbnail = ImageField()
    background = ImageField(required=False)


class WorldForm(ModelForm):
    class Meta:
        model = World
        fields = ['name', 'description', 'is_public', 'thumbnail', 'background']


class UniverseForm(ModelForm):
    class Meta:
        model = Universe
        fields = ['name', 'description', 'is_public', 'thumbnail', 'background']