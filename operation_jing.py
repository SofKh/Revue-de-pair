def operation(f1, f2):
    add = f1 + f2
    sou = f1 - f2
    div = f1 / f2
    return add, sou, div

f1 = 5.3
f2 = 2.6
a, s, d = operation(f1, f2)
print(f"l'addition de {f1} et {f2} est {a:.1f}")
print(f"la soustraction de {f1} et {f2} est {s:.2f}")
print(f"la division de {f1} et {f2} est {d:.3f}")

#Bonne organisation du code
