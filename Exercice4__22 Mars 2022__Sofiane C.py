# Exercice 4:

dico_cours2 = {}
file1 = open("bdd.txt", "r", encoding='utf8')
contenu = file1.read().split("\n")

dico_cours2[contenu[0]] = contenu[1]
dico_cours2[contenu[2]] = contenu[3]
dico_cours2[contenu[4]] = contenu[5]

file1.close()

print(dico_cours2)














