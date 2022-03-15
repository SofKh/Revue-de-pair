#Écrire un programme avec une fonction prenant 2 floats et retournant leur addition soustraction et division.
# Les résultats des additions doivent avoir au plus 1 chiffre après la virgule, la soustraction 2 chiffres après la virgule
# et la division 3 chiffres après la virgule.


def fonction(float1, float2):
 
    x = float1+float2
    y = float1-float2
    z = float1/float2
 
    return x, y, z

x, y, z = fonction(5.8, 7.2)


print(f"Le resultat est pour l'addition : {x:.1f}, pour la soustraction : {y:.2f} et division : {z:.3f}")



