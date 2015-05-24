from django.forms import Form, ModelForm

from .models import Universe, World, Place


class PlaceForm(ModelForm):
    class Meta:
        model = Place
        fields = ['name', 'description', 'is_public', 'thumbnail', 'background']


class WorldForm(ModelForm):
    class Meta:
        model = World
        fields = ['name', 'description', 'is_public', 'thumbnail', 'background']


class UniverseForm(ModelForm):
    class Meta:
        model = Universe
        fields = ['name', 'description', 'is_public', 'thumbnail', 'background']