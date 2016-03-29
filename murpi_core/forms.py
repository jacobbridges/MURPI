from django.forms import Form, ModelForm

from .models import Universe, World, Place, Roleplay, Scene, Character


class PlaceForm(ModelForm):
    class Meta:
        model = Place
        fields = ['name', 'description', 'is_public', 'image']


class WorldForm(ModelForm):
    class Meta:
        model = World
        fields = ['name', 'description', 'is_public', 'image']


class UniverseForm(ModelForm):
    class Meta:
        model = Universe
        fields = ['name', 'description', 'is_public', 'image']


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


class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'nick', 'race', 'image', 'home_world', 'description']