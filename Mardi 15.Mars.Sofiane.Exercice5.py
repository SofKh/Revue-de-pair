#Écrire un programme prenant l'année de naissance et lui retournant sa génération.



def generation():
    
    année=int(input("Indiquez votre année de naissance afin de savoir votre generation: "))
    if année >= 1946 and année < 1965:
        print("Vous etes de la generation Baby-boomers")
    elif année >= 1965 and année < 1980:
        print("Vous etes de la generation X")
    elif année >= 1980 and année < 2000:
        print("Vous etes de la generation Y")
    else:
        print("Vous etes de la generation Z")

generation()