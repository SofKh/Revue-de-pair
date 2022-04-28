
import random
import time

W = 15
L = 15 

class Board:
    def __init__(self):
        self.playerX = W-1
        self.playerY = 0
        self.board = [[None for j in range(L)] for i in range(W)]
        for i in range(W):
            for j in range(L):
                self.board[i][j] = GameObject()

        for i in range(0, W-2, 2):
            for j in range(0, L-2, 2):
                r_i = random.randint(i, i+1)
                r_j = random.randint(j, j+1)
                self.board[r_i][r_j] = Obstacle()
        for i in range(0, W-4, 4):
            r_i = random.randint(i, i+3)
            self.board[r_i][L-1] = Obstacle()
        for j in range(0, L-4, 4):
            r_j = random.randint(j, j+3)
            self.board[W-1][r_j] = Obstacle()

        self.board[0][L-1] = Exit()
        self.board[self.playerX][self.playerY] = Player()

    def start_game(self):
        self.menu()
        self.move()
            
    def __repr__(self):
        a = ""
        for grid in self.board:
            a += "|"
            a += "|".join(map(str, grid))
            a += "|"
            a += "\n"
        return a

    def menu(self):
        print("Welcome to the game")
    
    def success(self):
        print("You won")
        time.sleep(1000)
    
    def fail(self):
        print("You lost")
        time.sleep(1000)
    
    def move(self):
        f = False
        while not f:
            direction = int(input("Choisissez une direction 1.up, 2.down, 3.left, 4.right: "))
            if direction == 1:
                self.go_up()
            elif direction == 2:
                self.go_down()               
            elif direction == 3:
                self.go_left()               
            elif direction == 4:
                self.go_right()
            print(self.__repr__())

    def go_up(self):
        if -1 < self.playerX-1 < W:
            if self.board[self.playerX-1][self.playerY].isExit():
                self.success()
            elif not self.board[self.playerX-1][self.playerY].isEmpty():
                print("Il y a un obstacle, vous ne pouvez pas bouger vers haut")
            else:
                self.board[self.playerX-1][self.playerY] = Player()
                self.board[self.playerX][self.playerY] = GameObject()
                self.playerX -=1
                print("Bouger vers haut")
        else:
            print("Out of board, vous ne pouvez pas bouger")
        
    def go_down(self):
        if -1 < self.playerX+1 < W:
            if self.board[self.playerX+1][self.playerY].isExit():
                self.success()
            elif not self.board[self.playerX+1][self.playerY].isEmpty():
                print("Il y a un obstacle, vous ne pouvez pas bouger vers haut")
            else:
                self.board[self.playerX+1][self.playerY] = Player()
                self.board[self.playerX][self.playerY] = GameObject()
                self.playerX +=1
                print("Bouger vers bas")
        else:
            print("Out of board width, vous ne pouvez pas bouger")
    
    def go_left(self):
        if -1 < self.playerY-1:
            if self.board[self.playerX][self.playerY-1].isExit():
                self.success()
            elif not self.board[self.playerX][self.playerY-1].isEmpty():
                print("Il y a un obstacle, vous ne pouvez pas bouger vers haut")
            else:
                self.board[self.playerX][self.playerY-1] = Player()
                self.board[self.playerX][self.playerY] = GameObject()
                self.playerY -= 1
                print("Bouger vers gauche")

        else:
            print("Out of board length, vous ne pouvez pas bouger")    

    def go_right(self):
        if self.playerY+1 < L:
            if self.board[self.playerX][self.playerY+1].isExit():
                self.success()
            elif not self.board[self.playerX][self.playerY+1].isEmpty():
                print("Il y a un obstacle, vous ne pouvez pas bouger vers haut")
            else:
                self.board[self.playerX][self.playerY+1] = Player()
                self.board[self.playerX][self.playerY] = GameObject()
                self.playerY += 1
                print("Bouger vers droite")
        else:
            print("Out of board length, vous ne pouvez pas bouger") 

class GameObject:
    def __repr__(self):
        return f" "
    
    def isEmpty(self):
        return True
    
    def isExit(self):
        return False

class Player(GameObject):
    def __repr__(self):
        return f"▲"

class Obstacle(GameObject):
    def __repr__(self):
        return f"X"
    
    def isEmpty(self):
        return False
    
class Exit(GameObject):
    def __repr__(self):
        return f"◘"
    
    def isExit(self):
        return True

    def isEmpty(self):
        return False

board = Board()
print(board)
board.start_game()
