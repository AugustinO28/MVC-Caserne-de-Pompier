from django.db import models
 
class Equipement(models.Model):
    id_equip = models.CharField(max_length=100, primary_key=True)
    disponibilite = models.CharField(max_length=20)
    lieu_photo = models.CharField(max_length=200)
    def __str__(self):
        return self.id_equip
 
 
# Mise à jour de la disponibilité
def maj_disponibilite(ancien_lieu,nouveau_lieu):
        ancien_lieu.disponibilite = 'libre'
        ancien_lieu.save()
        if nouveau_lieu.id_equip != 'Caserne' : 
            nouveau_lieu.disponibilite = 'occupé'
            nouveau_lieu.save()

# Mise à jour du personnage
def maj_character(character, nouveau_etat, nouveau_lieu):
        character.etat = nouveau_etat
        character.lieu = nouveau_lieu
        character.save()

class Character(models.Model):
    etat_choices = [
        ('Disponible', 'Disponible'),
        ('En route', 'En route'),
        ('En mission', 'En mission'),
        ('Repos', 'Repos'),
        ('Fatigué', 'Fatigué'),
    ]

    id_character = models.CharField(max_length=100, primary_key=True)
    etat = models.CharField(max_length=20)
    photo = models.CharField(max_length=200)
    lieu = models.ForeignKey(Equipement, on_delete=models.CASCADE)
    def __str__(self):
        return self.id_character
        
    def se_preparer(self):
        ancien_lieu = self.lieu
        nouveau_lieu = Equipement.objects.get(id_equip='Parking de véhicules')
        if ancien_lieu.id_equip != 'Caserne':
            message = f"L'{self.id_character} doit être à la Caserne pour se préparer."
            return message, False

        elif nouveau_lieu.disponibilite == 'occupé' : 
            message = f"Impossible, le {nouveau_lieu.id_equip} est occupé."
            return message, False    
        
        elif self.etat != 'Disponible' : 
            message = f"Désolé, {self.id_character} n'est pas disponible."
            return message, False

        else :
            maj_disponibilite(ancien_lieu,nouveau_lieu)
            maj_character(self, 'En route', nouveau_lieu)
            message = f"Bravo ! {self.id_character} se prépare pour partir en mission."
            return message, True

    def partir_en_mission_1(self):
        ancien_lieu = self.lieu
        nouveau_lieu = Equipement.objects.get(id_equip='Lieu d\'intervention 1')
        
        if ancien_lieu.id_equip != 'Parking de véhicules':
            message = f"L'{self.id_character} doit être au Parking de véhicules pour partir en mission."
            return message, False     
        
        elif nouveau_lieu.disponibilite == 'occupé':
            message = f"Impossible, une équipe s'est déjà rendue sur le {nouveau_lieu.id_equip}."
            return message, False           

        elif self.etat != 'En route':
            message = f"Désolé, l'{self.id_character} n'est pas en route."
            return message, False

        else:
            maj_disponibilite(ancien_lieu, nouveau_lieu)
            maj_character(self, 'En mission', nouveau_lieu)
            message = f"Bravo ! L'{self.id_character} part en mission vers le {nouveau_lieu.id_equip}."
            return message, True

    def partir_en_mission_2(self):
        ancien_lieu = self.lieu
        nouveau_lieu = Equipement.objects.get(id_equip='Lieu d\'intervention 2')

        if ancien_lieu.id_equip != 'Parking de véhicules':
            message = f"L'{self.id_character} doit être au Parking de véhicules pour partir en mission."
            return message, False

        elif nouveau_lieu.disponibilite == 'occupé':
            message = f"Impossible, une équipe s'est déjà rendue sur le {nouveau_lieu.id_equip}."
            return message, False
            
        elif self.etat != 'En route':
            message = f"Désolé, l'{self.id_character} n'est pas en route."
            return message, False

        else:
            maj_disponibilite(ancien_lieu, nouveau_lieu)
            maj_character(self, 'En mission', nouveau_lieu)
            message = f"Bravo ! L'{self.id_character} part en mission vers le {nouveau_lieu.id_equip}."
            return message, True

    def rentrer_de_mission(self):
        ancien_lieu = self.lieu
        nouveau_lieu = Equipement.objects.get(id_equip='Caserne')
        if self.etat != 'En mission':
            message = f"Désolé, l'{self.id_character} n'est pas en mission."
            return message, False

        elif ancien_lieu.id_equip not in ['Lieu d\'intervention 1', 'Lieu d\'intervention 2']:
            message = f"L'{self.id_character} doit être sur un lieu d'intervention pour rentrer de mission."
            return message, False

        else:
            maj_disponibilite(ancien_lieu, nouveau_lieu)
            maj_character(self, 'Fatigué', nouveau_lieu)
            message = f"Bravo ! L'{self.id_character} rentre de mission et est maintenant fatiguée."
            return message, True

    def se_reposer(self):
        ancien_lieu = self.lieu
        nouveau_lieu = Equipement.objects.get(id_equip='Maison')

        if self.etat != 'Fatigué':
            message = f"Désolé, l'{self.id_character} n'est pas fatiguée."
            return message, False

        elif ancien_lieu.id_equip != 'Caserne':
            message = f"L'{self.id_character} doit être à la Caserne pour se reposer."
            return message, False

        elif nouveau_lieu.disponibilite == 'occupé':
            message = f"Impossible, la {nouveau_lieu.id_equip} est occupée."
            return message, False

        else:
            maj_disponibilite(ancien_lieu, nouveau_lieu)
            maj_character(self, 'Repos', nouveau_lieu)
            message = f"Bravo ! L'{self.id_character} se repose à la maison."
            return message, True

    def aller_au_travail(self):
        ancien_lieu = self.lieu
        nouveau_lieu = Equipement.objects.get(id_equip='Caserne')
        if ancien_lieu.id_equip != 'Maison':
            message = f"L'{self.id_character} est déjà au travail."
            return message, False        

        elif self.etat != 'Repos':
            message = f"Désolé, l'{self.id_character} n'est pas en repos."
            return message, False

        else:
            maj_disponibilite(ancien_lieu, nouveau_lieu)
            maj_character(self, 'Disponible', nouveau_lieu)
            message = f"Bravo ! L'{self.id_character} est de retour au travail."
            return message, True


    
    

    