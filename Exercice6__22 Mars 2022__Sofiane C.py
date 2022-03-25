# Exercice 6:
# Offrir à l'utilisateur une nouvelle option au menu lui permettant d'ajouter un cours et un nom d'enseignant
# à la base de données de l'exercice 4. Une fois les données utilisateurs entrées,
# ajouter les informations à la fin du document bdd.txt


dico_cours2 = {}
file1 = open("bdd.txt", "r", encoding='utf8')
contenu = file1.read().split("\n")

dico_cours2[contenu[0]] = contenu[1]
dico_cours2[contenu[2]] = contenu[3]
dico_cours2[contenu[4]] = contenu[5]

file1.close()

print(dico_cours2)


dico_cours = {"Keven Presseau-St-Laurent": "Concepts de programmation 1",
              "Emma Senez": "Logique Mathématiques",
              "Fisset J": "Systeme d'exploitation"}

print("Choisissez une option parmis les suivantes: ")
print("#1 Cours de Concepts de programmation 1")
print("#2 Cours de Logique Mathématiques")
print("#3 Cours de Systeme d'exploitation")
print("#4 Rechercher un enseignant")
print("#5 Ajouter un enseignant et un cours à la base de donnée")

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
elif utilisateur == 5:
    nouveau_prof = input("Precisez le nom du nouveau professeur: ")
    nouveau_cours = input("Précisez le nom du nouveau cours")
    with open("bdd.txt", "a", encoding='utf8') as file:
        file.write("\n")
        file.write(f"{nouveau_prof}\n")
        file.write(f"{nouveau_cours}\n")
        file.close()