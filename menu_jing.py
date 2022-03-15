def menu():
    choix = int(input("Entrez votre choix, 1 for Bonjour, 2 for Au revoir, 3 for A plus tard: "))
    match choix:
        case 1: print("Bonjour")
        case 2: print("Au revoir")
        case 3: print("A plus tard")
        case _: print("Choix invalide")
    return None

menu()