from django import forms
 
from .models import Character
 
action_choices = [
    ('aller_au_travail', 'Aller au travail'),
    ('se_preparer', 'Se préparer'),
    ('se_reposer', 'Se reposer'),
    ('partir_en_mission_1', 'Partir en mission 1'),
    ('partir_en_mission_2', 'Partir en mission 2'),
    ('rentrer_de_mission', 'Rentrer de mission'),
]

class MoveForm(forms.ModelForm):
    action = forms.ChoiceField(choices=action_choices, label='Action')
    class Meta:
        model = Character
        fields = ['action']
        