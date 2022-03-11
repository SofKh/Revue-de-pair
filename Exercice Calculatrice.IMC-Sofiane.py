# Créer une calculatrice d'IMC demandant à l'utilisateur sa grandeur(en mètres), son poids(en kg).
# Retournez ensuite la catégorie dans laquelle se trouve la personne.

import math

def calcul_imc():

    taille = float(input("Veuillez entrer votre taille en metre: "))
    poids = int(input("Veuillez entrer votre poids en kg: "))
    
    return poids / taille**2

def imc(resultat):
    if resultat < 18.5 :
        print("Votre categorie IMC est Poids Insuffisant")
    
    elif resultat <= 24.9 :
        print("Votre categorie IMC est Poids Normal")
    
    elif resultat <= 29.9 :
        print("Votre categorie IMC est Embonpoint")
    
    elif resultat <= 34.9 :
        print("Votre categorie IMC est Embonpoint")

    elif resultat <= 39.9 :
        print("Votre categorie IMC est Embonpoint")
    
    elif resultat >= 40.0 :
        print("Votre categorie IMC est Embonpoint")
    
    return None

x=calcul_imc()
imc(x)




    






