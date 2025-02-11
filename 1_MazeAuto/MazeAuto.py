import os
import time
import keyboard
import random

class maze:
    def __init__(self) -> None:
        self.maze = [
                    ["X", "X", "X", "X", "X", "X", "X"],
                    ["X", " ", " ", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", "X", " ", " "],
                    ["X", " ", "X", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", " ", " ", "X"],
                    ["X", " ", "X", "X", "X", "X", "X"],
                    ]
        self.ply = pos(5, 1)
        self.end = pos(2, 6)
        self.maze[self.ply.y][self.ply.x] = "P"
        self.maze[self.end.y][self.end.x] = "E"
    
    def isInBound(self, y, x):
        if y>=0 and x>=0 and y<len(self.maze) and x<len(self.maze[0]):
            return True
        else:
            return False
    
    def print(self):
        os.system("cls")
        print("\n\n\n")
        for row in self.maze:
            for col in row:
                print(col," ", end="")
            print("")
        print("\n\n\n")
    
    def printEND(self):
        #os.system("cls")
        print("\n\n\n")
        print(">>>>> Congraturation!!! <<<<<")
        print("\n\n\n")
        keyboard.wait("")

    def move_up(self):
        next_move = pos(self.ply.y-1, self.ply.x)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.50)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True
    
    def move_down(self):
        next_move = pos(self.ply.y+1, self.ply.x)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.50)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True

    def move_left(self):
        next_move = pos(self.ply.y, self.ply.x-1)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.50)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True

    def move_right(self):
        next_move = pos(self.ply.y, self.ply.x+1)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.50)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True

    def move_upordown(self,oldkey):
        k_next = " "
        next_up = pos(self.ply.y-1, self.ply.x)
        if not self.isInBound(next_up.y,next_up.x):
            next_up = self.ply
        next_down = pos(self.ply.y+1, self.ply.x)
        if not self.isInBound(next_down.y,next_down.x):
            next_down = self.ply

        if oldkey == "w" or oldkey == " ":
            if self.maze[next_up.y][next_up.x] == " " or self.maze[next_up.y][next_up.x] == "E":
                k_next = "w"
            elif self.maze[next_down.y][next_down.x] == " " or self.maze[next_down.y][next_down.x] == "E":    
                k_next = "s"    
            else:
                k_next = " "                    
        elif oldkey == "s" or oldkey == " ":
            if self.maze[next_down.y][next_down.x] == " " or self.maze[next_down.y][next_down.x] == "E" :    
                k_next = "s"        
            elif self.maze[next_up.y][next_up.x] == " " or self.maze[next_up.y][next_up.x] == "E":
                k_next = "w"
            else:
                k_next = " "                
        else:
            k_next = " "

        return k_next

    def move_leftorright(self,oldkey):
        k_next = " "
        next_left = pos(self.ply.y, self.ply.x-1)
        if not self.isInBound(next_left.y,next_left.x):
            next_left = self.ply
        next_right = pos(self.ply.y, self.ply.x+1)
        if not self.isInBound(next_right.y,next_right.x):
            next_right = self.ply


        if oldkey == "a" or oldkey == " ":
            if self.maze[next_left.y][next_left.x] == " " or self.maze[next_left.y][next_left.x] == "E":    
                k_next = "a"        
            elif self.maze[next_right.y][next_right.x] == " " or self.maze[next_right.y][next_right.x] == "E":    
                k_next = "d"        
            else:
                k_next = " "                
        elif oldkey == "d" or oldkey == " ":
            if self.maze[next_right.y][next_right.x] == " " or self.maze[next_right.y][next_right.x] == "E":    
                k_next = "d"        
            elif self.maze[next_left.y][next_left.x] == " " or self.maze[next_left.y][next_left.x] == "E":    
                k_next = "a"
            else:
                k_next = " "                        
        else:
            k_next = " "

        return k_next        

class pos:
    def __init__(self) -> None:
        self.y = None
        self.x = None
    
    def __init__(self, y, x) -> None:
        self.y = y
        self.x = x

if __name__ == '__main__':

    m = maze()
    m.print()

    d = 1 #Keep direction 1 (up,down) or 2(left,right)

    ukey = " "
    rkey = " "
    keep_key = ""

    while True:
        k1 = m.move_upordown(ukey)
        k2 = m.move_leftorright(rkey)

        if d == 1:
            if k2 != " ":
                d = 2
                k = k2
                rkey = k2
            else:
                k = k1                           
                ukey = k1
        elif d == 2:
            if k1 != " ":
                d = 1
                k = k1
                ukey = k1
            else:
                k = k2                
                rkey = k2
        else:            
            d = 1
            k = k1
            ukey = k1

        keep_key = keep_key + "->" + k

        if k == "w":
            if m.move_up():
                m.print()
                print(keep_key)
        elif k == "s":
            if m.move_down():
                m.print()
                print(keep_key)
        elif k == "a":
            if m.move_left():
                m.print()
                print(keep_key)
        elif k == "d":
            if m.move_right():
                m.print()  
                print(keep_key)
