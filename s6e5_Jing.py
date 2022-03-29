import copy

# Entrez le nom de fichier
def entrer_nom_f():
    return input("Entrez un nom de fichier: ")
     
# Entrez un nombre illimité de nombres positif
def entrer_listnbr():
    liste_nbr = []
    while True:
        num = int(input("Entrez un nombre positif: "))
        if num >= 0:
            liste_nbr.append(num)
        else:
            break
    return liste_nbr

# La liste en ordre croissant
def trier_croissant(list_num):
    for i in range(len(list_num)):
        for j in range(i+1, len(list_num)):
            if list_num[i] >= list_num[j]:
                temp = list_num[i]
                list_num[i] = list_num[j]
                list_num[j] = temp
    return copy.deepcopy(list_num)

# La liste en ordre décroissant
def trier_decroissant(list_num):
    for i in range(len(list_num)):
        for j in range(i+1, len(list_num)):
            if list_num[i] <= list_num[j]:
                temp = list_num[i]
                list_num[i] = list_num[j]
                list_num[j] = temp
    return copy.deepcopy(list_num)

# Le maximum
def num_max(list_num):
    max = list_num[0]
    for i in range(1, len(list_num)):
        if max <= list_num[i]:
            max = list_num[i]
    return max

# Le minimum
def num_min(list_num):
    min = list_num[0]
    for i in range(1, len(list_num)):
        if min >= list_num[i]:
            min = list_num[i]
    return min

# La moyenne de la liste
def num_moy(list_num):
    sum = 0
    for num in list_num:
        sum = sum + num
    return sum / len(list_num)

# La médiane
def num_mediane(list_num):
    mid_index = int(len(list_num) / 2)
    if len(list_num) % 2 != 0:
        mediane = list_num[mid_index]
    else:
        mediane = (list_num[mid_index - 1] + list_num[mid_index]) / 2
    return mediane

# Le mode
def num_mode(list_num):
    dic_num = {}
    for num in list_num:
        if num in dic_num:
            dic_num[num] += 1
        else:
            dic_num[num] = 1
    max = list(dic_num.values())[0]
    for k, v in dic_num.items():
        if max < v:
            max = v
            key = k
    return key, max
        
l_num = entrer_listnbr()
l_num_croi = trier_croissant(l_num)
l_num_decr = trier_decroissant(l_num)
num_max = num_max(l_num)
num_min = num_min(l_num)
num_moy = num_moy(l_num)
num_mediane = num_mediane(l_num_croi)
nom_mode = num_mode(l_num)

nom_f = entrer_nom_f()
with open(nom_f, "w") as f_out:
    f_out.write(f"{l_num_croi}\n{l_num_decr}\n{num_max}\n{num_min}\n{num_moy}\n{num_mediane}\n{nom_mode}\n")
