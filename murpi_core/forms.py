from django import forms


class PlaceForm(forms.Form):
    name = forms.CharField(max_length=40)
    description = forms.CharField(widget=forms.Textarea)
    is_public = forms.BooleanField(widget=forms.CheckboxInput, required=False, initial=True)
    thumbnail = forms.ImageField()
