dic_cours = {}
with open("bdd.txt", "r") as filin:
    lists = filin.read().split("\n")
    for i in range(1, len(lists), 2):
        key = lists[i-1]
        value = lists[i]
        dic_cours[key] = value
    print(dic_cours)

print("ci-dessous est le menu de cours:")
for i, v in enumerate(dic_cours.values()):
    print(i, v)
print("3 Entrez le nom de professeur pour fair une recherche")
print("4 Ajoutez le nom de professeur et un cours")
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
elif choix == 4:
    kin = input("Entrez le nom de professeur: ")
    vin = input("Entrez le cours: ")
    with open("bdd.txt", "a") as fila:
        fila.write("\n")
        fila.write(f"{kin}\n")
        fila.write(f"{vin}\n")
