dic_cours = {"Keven Presseau-St-Laurent": "Concepts de programmation 1",
            "Emma Parent Senez": "Logique mathématique pour les professionnels de l'informatiq",
             "Jean-Pierre Fiset": "Systèmes d'exploitation"
}

print("ci-dessous est le menu de cours:")
for i, v in enumerate(dic_cours.values()):
    print(i, v)
print("3 Entrez le nom de professeur pour fair une recherche")
choix = int(input("Entrez votre choix: "))
if choix == 0:
    print("Keven Presseau-St-Laurent: ", dic_cours["Keven Presseau-St-Laurent"])
elif choix == 1:
    print("Emma Parent Senez: ", dic_cours["Emma Parent Senez"])
elif choix == 2:
    print("Jean-Pierre Fiset: ", dic_cours["Jean-Pierre Fiset"])
elif choix == 3:
    nom_prof = input("Entrez le nom de professeur: ")
    f = False
    for k in dic_cours.keys():
        if nom_prof == k:
            f = True
    if f == True:
        print(nom_prof, ": ", dic_cours[nom_prof])
    else:
        print("l'enseignant n'est pas présent dans la liste de cours.")