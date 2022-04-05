from time import sleep
import os, random

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def draw_line():
    line = "-"
    for i in range(10):
        line = line + "-" 
        print(line, end="")
        sleep(0.2)
    print("\n")

def draw_pyramid():
    for i in range(1, 20, 2):
        star = "*"*i
        print(f"{star:^20}")
        sleep(0.3)

def turn_arrow():
    for i in range(4):
        arrow = "🡲"
        if i == 1:
            arrow = "🡱"
        if i == 2:
            arrow = "🡸"
        if i == 3:
            arrow = "🡻"
        print(f"\r{arrow:>10}",end="")
        sleep(0.5)
    print("\n")

def show_radom_digit():
    for i in range(10):
        digit = random.randint(0, 20)
        space = " "*random.randint(0, 20)
        print(f"{space}{digit}")
        sleep(0.5)

def bird_fly():
    frames = ["\(^u^)/",
         "_(^u^)_",
         "_(^.^)_",
         "\(^.^)/"
         ]
    i = 0
    for time_instant in range(25):
        print("\r" + frames[i], end="")
        sleep(0.2)
        i = (i + 1) % len(frames)
    print("\n")

def menu():
    exit = False
    while not exit:
        print("Choisir une des animations suivantes: ")
        print("1. draw a line")
        print("2. draw a pyramid")
        print("3. turn arrow's direction")
        print("4. show radom digit in radom place")
        print("5. bird fly")
        print("6. Sortir du jeu")
        choix = int(input("Écrire votre choix: "))
        if choix == 1:
            draw_line()
        if choix == 2:
            draw_pyramid()
        if choix == 3:
            turn_arrow()
        if choix == 4:
            show_radom_digit()
        if choix == 5:
            bird_fly()
        if choix == 6:
            exit = True

menu()
# nice animations !! good job :)
