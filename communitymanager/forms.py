from django import forms

from .models import *


class CommentaireForm(forms.Form):
    contenu = forms.CharField(required=True)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ["auteur"]
        widgets = {
            'date_evenement': forms.DateTimeInput(attrs={
                'class': 'form-control', 'type': 'datetime-local',
            }, format="%Y-%m-%dT%H:%M"),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["date_evenement"].input_formats = ["%Y-%m-%dT%H:%M"]

    """
    def clean(self):

        cleaned_data = super(PostForm, self).clean()
        date_evenement = cleaned_data['date_evenement']
        evenementiel = cleaned_data['evenementiel']

        if date_evenement < timezone.now() and evenementiel :
            raise forms.ValidationError('Votre événement doit se passer dans le futur !')
        return cleaned_data
    """


class CommunauteForm(forms.ModelForm):
    class Meta:
        model = Communaute
        exclude = ["abonnes", "suspended"]


class CalendarForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ["auteur", "evenementiel"]
        widgets = {
            'date_evenement': forms.DateTimeInput(attrs={
                'class': 'form-control', 'type': 'datetime-local',
            }, format="%Y-%m-%dT%H:%M"),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["date_evenement"].input_formats = ["%Y-%m-%dT%H:%M"]


#Form pour le fitlrage de l'affichage des posts :
class PrioriteForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(PrioriteForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['label'].required = False

    évènement = forms.BooleanField(required=False)

    class Meta:
        model = Priorite
        fields = ['label']


