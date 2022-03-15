#Écrire un programme demandant un entier à un utilisateur et lui retournant sa parité. Ex.: Le nombre «4» est paire.

def parite():
    entier=int(input("Rentrez un nombre entier: "))
    if entier%2==0:
        print("Le nombre est paire")
    else:
        print("Le nombre est impaire")

    return None

parite()


