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
choix = int(input("Entrez votre choix: "))
if choix == 0:
    print("Keven Presseau-St-Laurent: ", dic_cours["Keven Presseau-St-Laurent"])
elif choix == 1:
    print("Emma Parent Senez: ", dic_cours["Emma Parent Senez"])
elif choix == 2:
    print("Jean-Pierre Fiset: ", dic_cours["Jean-Pierre Fiset"])