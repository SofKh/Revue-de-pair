dic_cours = {}
with open("bdd.txt", "r") as filin:
    lists = filin.read().split("\n")
    for i in range(1, len(lists), 2):
        key = lists[i-1]
        value = lists[i]
        dic_cours[key] = value
    print(dic_cours)
    
    # bonne organisation du code
