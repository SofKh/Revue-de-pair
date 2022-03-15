#Écrire une fonction prenant deux nombres et vérifiant si le premier nombre est plus petit que le deuxième
#si ce n'est pas le cas, les retourner dans l'ordre inverse. Ex.: fonction(4, 3) retournerait 3 et, ensuite, 4.

def fonction(nbr1, nbr2):
    if nbr1<nbr2:
        return nbr1, nbr2
    else:
        return nbr2, nbr1

nbr1=1
nbr2=3

fonction(1,3)




