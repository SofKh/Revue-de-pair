# Exercice 3:
# Créer un dictionnaire possédant les cours que vous suivez cette session et leur enseignant respectif. Par exemple:
# Keven Presseau-St-Laurent - Concepts de programmation 1
# Ensuite, afficher un menu à la console présentant les 3 cours et offrant à l'utilisateur d'en sélectionner 1
# Lorsque l'utilisateur à fait sa sélection, afficher le nom de l'enseignant et le nom du cours à l'écran.

dico_cours = {"Keven Presseau-St-Laurent": "Concepts de programmation 1", 
            "Emma Senez": "Logique Mathématiques", "Fisset J": "Systeme d'exploitation"}

print("Veuillez sélectionner votre cours parmis les choix proposés: ")
print("#1 Concepts de programmation 1")
print("#2 Logique Mathématiques")
print("#3 Systeme d'exploitation")

utilisateur = int(input("Veuillez rentrer votre choix: "))

if utilisateur == 1:
    print(dico_cours.get("Keven Presseau-St-Laurent"))
    print("Keven Presseau-St-Laurent")
elif utilisateur == 2:
    print(dico_cours.get("Emma Senez"))
    print("Emma Senez")
elif utilisateur == 3:
    print(dico_cours.get("Fisset J"))
    print("Fisset J")
else:
    print("Merci de rentrer un des choix proposés")

    