import random

class Map(object):
    def __init__(self, rows, cols, no_mines):
        self.rows = rows
        self.cols = cols
        self.no_mines = no_mines
        
        temp = [False for _ in range(cols)]
        self.grid = [temp.copy() for _ in range(rows)]
        
        self.create_and_mines()
        self.game = self.get_numbers_()
    
    
    # to create rows * cols grid with mines randomly placed
    def create_and_mines(self): 
        postions = []
        while len(postions) < self.no_mines:
            x = random.randint(0, self.rows - 1)
            y = random.randint(0, self.cols - 1)
            if(self.grid[x][y]):
                continue
            else:
                self.grid[x][y] = True
                postions.append((x, y))
                
    def no_adjacent_mines(self, x, y):
        count = 0
        dis = [-1, 0, 1]
        for diffx in dis:
            for diffy in dis:
                X = x + diffx
                Y = y + diffy
                if(X >= 0 and Y >= 0 and X < self.rows and Y < self.cols and self.grid[X][Y]):
                    count += 1 
        if(self.grid[x][y]):
            count -= 1
        return count    

    def get_numbers_(self):
        temp = [0 for _ in range(self.cols)]
        game = [temp.copy() for _ in range(self.rows)]
        for r in range(self.rows):
            for c in range(self.cols):
                game[r][c] = self.no_adjacent_mines(r, c)
        return game

    def print_grid(self):
        for r in range(self.rows):
            for c in range(self.cols):
                print(self.game[r][c], end=" ")
            print("")
        
        
if __name__ == "__main__":
    map = Map(5, 5, 2)
    map.print_grid()    
    
    
    
    
    
(open | cloes)
if(open): print(count)
if(cols): ""    


while(user_cliks):
    if it is in mine:
        game Over
    closed --> open    
    if there is no hidden cell
        he wins:
        