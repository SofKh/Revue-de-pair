def premier():
    num = int(input("Entrez un nombre entre 1 et 20: "))
    if 1 <= num <= 20:
        print("ce nombre est bel et bien entre 1 et 20")
    else:
        print("ce nombre n'est pas entre 1 et 20")
    if num == 1 or num == 2 or num == 3 or num == 5 or num == 7 or num == 11 or num == 13 or num == 17 or num == 19:
        print(f"{num} est un nombre premier")
    else:
        print(f"{num} n'est pas un nombre premier")
    return None

premier()

# Bonne utilisation du f"{}
