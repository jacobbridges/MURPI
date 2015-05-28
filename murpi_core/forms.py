from django.forms import Form, ModelForm

from .models import Universe, World, Place, Roleplay, Scene


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


class RoleplayForm(ModelForm):
    class Meta:
        model = Roleplay
        fields = ['name', 'short_description', 'description', 'plain_rules', 'is_public', 'status']


class SceneFormForPlaceView(ModelForm):
    class Meta:
        model = Scene
        fields = ['name', 'short_description', 'roleplay']


class SceneFormForRPView(ModelForm):
    class Meta:
        model = Scene
        fields = ['name', 'short_description', 'place']