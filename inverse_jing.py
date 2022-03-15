def verifi(n1, n2):
    if n1 > n2:
        temp = n1
        n1 = n2
        n2 = temp
    return n1, n2

num1 = 4
num2 = 3
print(verifi(num1, num2))