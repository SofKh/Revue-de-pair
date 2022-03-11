# Créer une calculatrice d'IMC demandant à l'utilisateur d'entrer son âge, sa grandeur(en mètres), son poids(en kg) et son sexe. 
# Retournez ensuite la catégorie dans laquelle se trouve la personne.

def entre_num():
    grandeur = float(input("Entrez votre grandeur(en mètres): "))
    poids = float(input("Entrez votre poids(en kg): "))
    return grandeur, poids

def calcu_imc(grandeur, poids):
    return poids / grandeur**2

def categorie(imc):
    if imc < 16:
        return "Maigreur extrême"
    elif imc < 18.5:
        return "Maigreur"
    elif imc < 24.9:
        return "Poids normal"
    elif imc < 29.9:
        return "Embonpoint"
    elif imc < 34.9:
        return "Obésité, classe 1"
    elif imc < 39.9:
        return "Obésité, classe 2"
    else:
        return "Obésité, classe 3 (obésité morbide)"

grandeur, poids = entre_num()
imc = calcu_imc(grandeur, poids)
print(f"votre grandeur est {grandeur} m, votre poids est {poids} kg, vous etes {categorie(imc)}")
