# Exercice 5: En se basant sur l'exercice 4, modifier le menu utilisateur en y ajoutant une option lui permettant
# de faire une recherche d'enseignant. Vérifier si l'enseignant entré par l'utilisateur est présent dans votre
# liste de cours et indiquer le résultat à la console.

dico_cours = {"Keven Presseau-St-Laurent": "Concepts de programmation 1",
              "Emma Senez": "Logique Mathématiques",
              "Fisset J": "Systeme d'exploitation"}

print("Choisissez une option parmis les suivantes: ")
print("#1 Cours de Concepts de programmation 1")
print("#2 Cours de Logique Mathématiques")
print("#3 Cours de Systeme d'exploitation")
print("#4 Rechercher un enseignant")

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
elif utilisateur == 4:
    choix_enseignant = input("Rentrer le nom de l'enseignant: ")
    f = False
    for professeur in dico_cours.keys():
        if choix_enseignant == professeur:
            f = True
    if f is True:
        print(choix_enseignant, ": ", dico_cours[choix_enseignant])
    else:
        print("L'enseignant n'est pas présent dans la liste de cours.")

        