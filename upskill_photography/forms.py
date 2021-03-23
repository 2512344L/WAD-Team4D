from django import forms
from .models import Picture
class uploading(forms.modelForm):
    class Meta:
        model = Picture
        fields = ('uploading_user', 'title', 'image')


