from django.shortcuts import render, get_object_or_404, redirect
from .forms import MoveForm
from .models import Equipement, Character
from django.contrib import messages

def character_equipement(request):
    characters = Character.objects.all().order_by('id_character')
    lieux = Equipement.objects.all().order_by('id_equip')
    context = {
        'characters': characters,
        'lieux': lieux
    }
    return render(request, 'caserne/character_equipement.html', context)

def character_detail(request, name):
    character = get_object_or_404(Character, id_character=name)
    lieux = Equipement.objects.all().order_by('id_equip')
    message = ''
    form=MoveForm()
    if request.method == 'POST':
        form = MoveForm(request.POST, instance=character)
        if form.is_valid():
            action = form.cleaned_data['action']

            if action == 'se_preparer':
                message, success = character.se_preparer()
            elif action == 'partir_en_mission_1':
                message, success = character.partir_en_mission_1()
            elif action == 'partir_en_mission_2':
                message, success = character.partir_en_mission_2()
            elif action == 'rentrer_de_mission':
                message, success = character.rentrer_de_mission()
            elif action == 'se_reposer':
                message, success = character.se_reposer()
            elif action == 'aller_au_travail':
                message, success = character.aller_au_travail()
            else:
                message = "Action inconnue."
                success = False

            if success:
                messages.success(request, message)
                return redirect('character_detail', name=character.id_character)
            else:
                messages.error(request, message)

        else:
            message = "Formulaire invalide."
    
    return render(request,'caserne/character_detail.html',{'character': character,'lieux': lieux, 'form': form, 'message': message})


