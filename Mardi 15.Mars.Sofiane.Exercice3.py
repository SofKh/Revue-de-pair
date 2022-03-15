# Écrire un programme offrant un menu à un utilisateur avec 3 choix et lui affichant la phrase suivante une fois sélectionné:
# 1. Bonjour
# 2. Au revoir
# 3. À plus tard


def menu():
    print("Voici vos choix: ")
    print("#1. Bonjour")
    print("#2. Au revoir")
    print("#3. A plus tard")
    
    choix=int(input("Veuillez choisir une proposition parmis les choix proposés: "))
    
    if choix ==1 :
        print("Bonjour")
    elif choix == 2:
        print("Au revoir")
    elif choix == 3 :
        print("A plus tard")
    else:
        print("Non valide")
    
    return None

menu()





