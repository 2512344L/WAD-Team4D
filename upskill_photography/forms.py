from django import forms
from upskill_photography.models import Picture

class uploading(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ('uploading_user', 'title', 'image')


