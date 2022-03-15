#Écrire un programme demandant à l'utilisateur de rentrer un nombre entre 1 et 20,
# vérifier si ce dernier est bel et bien entre 1 et 20 et indiquez-lui
#si son nombre est un nombre premier (ayant aucun autre facteur entier que 1 et lui-même)

def nombres():
    
    choix=int(input("Veuillez entrer un nombre entre 1 et 20: "))

    if 1 <= choix <= 20:
        print("Ce nombre est bien entre 1 et 20")
    else:
        print("Ce nombre n'est pas entre 1 et 20")
    
    if choix == 2 or choix == 3 or choix == 5 or choix == 7 or choix == 11 or choix == 13 or choix == 17 or choix == 19:
        print("Et c'est un nombre premier")

    return None

nombres()







