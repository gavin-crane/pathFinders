# Set the whole map to all walls. Select an entrance and an exit, setting these two locations to no walls;
# Randomly choose a wall and flip it to no wall;
# Test whether the exit is accessible from the entrance with BFS/DFS;
# If not accessible then goto 2 else goto 5;
# Maze is successfully created.
import pygame
import time
import random
import numpy as np

class MakeMaze():
    
    foundDest = False
    
    def __init__(self, grid, start, dest, sqwidth, scr):
        
        
        self.start = start
        self.dest = dest
        self.sqwidth = sqwidth
        
        self.width = len(grid[0])
        self.height = len(grid)
        
        #print("Width {0}, Height {1}".format(self.width, self.height))
        
        self.visualizeMaze(grid, start, dest, scr, sqwidth)

    def visualizeMaze(self, grid, start, dest, scr, sqwidth):
        
        allTiles = [] # build  alist of all the possible indices in the grid
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                allTiles.append((i, j))
                
        print(allTiles)
    
        while not MakeMaze.foundDest: # randomly remove walls until a path is found from start to dest
            
            # randRow = random.randint(0, len(grid)-1)
            # randCol = random.randint(0, len(grid[0])-1)
            
            randomIndices = random.choice(allTiles)
            allTiles.remove(randomIndices)
            grid[randomIndices[0]][randomIndices[1]].isWall = False
            
            pygame.event.get()
            
            if not grid[randomIndices[0]][randomIndices[1]].isStartNode and not grid[randomIndices[0]][randomIndices[1]].isEndNode:
                pygame.draw.rect(scr, (255, 255, 255), [grid[randomIndices[0]][randomIndices[1]].sqx, grid[randomIndices[0]][randomIndices[1]].sqy, self.sqwidth-1, self.sqwidth-1])
            pygame.display.update()
    
            
            visited = [[False] * len(grid[1]) for _ in range(len(grid))]
              
            self.isThereAPathDFS(start[0], start[1], dest, grid, visited, scr)  
           
            print("still finding paths")
        print("Found maze path")
        
    def isThereAPathDFS(self, row, col, dest, grid, visited, scr):
        if np.array_equal(dest, [row, col]):
            print("found dest!")
            MakeMaze.foundDest = True
            return True
        
        elif not MakeMaze.foundDest:
            # row 21
            #print("baordHeight", self.boardHeight, "board" )
            if row < 0 or col < 0 or row > len(grid)-1 or col > len(grid[0])-1:
                return
            elif grid[row][col].isWall or visited[row][col] :
                return
            
            visited[row][col] = True
            
            #grid[row][col].isPath = True
            
            
            # draw path to screen 
            #pygame.draw.rect(scr, (0, 120, 0), [grid[row][col].sqx, grid[row][col].sqy, self.sqWidth-1, self.sqWidth-1])
            # time.sleep(.001)
            # pygame.display.update()
            
            # time.sleep(.001)
            # pygame.event.get()
            # pygame.draw.rect(scr, (143, 126, 191), [grid[row][col].sqx, grid[row][col].sqy, self.sqwidth-1, self.sqwidth-1])
            # pygame.display.update()
            
            
            # up
            self.isThereAPathDFS(row-1, col, dest, grid, visited, scr)
            
            # down
            self.isThereAPathDFS(row+1, col, dest, grid, visited, scr)
            # left

            self.isThereAPathDFS(row, col-1, dest, grid, visited, scr)
            # right

            self.isThereAPathDFS(row, col+1, dest, grid, visited, scr)
        return False