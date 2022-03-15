def gene(ann_nai):
    generation = ""
    if 1946 <= ann_nai <= 1965:
        generation = "Les Baby-boomers"
    elif 1966 <= ann_nai <= 1979:
        generation = "La generation X"
    elif 1980 <= ann_nai <= 1999:
        generation = "La generation Y"
    elif ann_nai >= 2000:
        generation = "La generation Z"
    return generation

annee = 1987
print(f"Votre annee de naissance est {annee}, vous est dans {gene(annee)}")
