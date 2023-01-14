import pygame
import time
import numpy as np


class DFS():
    
    foundDest = False

    def __init__(self, grid, start, dest, GRID_HEIGHT, GRID_WIDTH, sqWidth, scr):
        
        self.boardHeight = GRID_HEIGHT
        self.boardWidth = GRID_WIDTH
        self.sqWidth = sqWidth
        self.start = start
        self.dest = dest
        
        visited = [[False] * self.boardHeight for _ in range(self.boardWidth)]
        
        if (self.DFSAlgo(start[0], start[1], dest, grid, visited, scr)):
            print("hello this is the end of DFS================================")
         
    def DFSAlgo(self, row, col, dest, grid, visited, scr):
            
        print("row",row, "col",col, "DFS.foundDest", DFS.foundDest)
    
        if np.array_equal(dest, [row, col]):
            print("found dest!")
            DFS.foundDest = True
            return
        
        elif not DFS.foundDest:
        
            # row 21
            #print("baordHeight", self.boardHeight, "board" )
            if row < 0 or col < 0 or row > self.boardWidth-1 or col > self.boardHeight-1:
                return
            elif grid[row][col].isWall or visited[row][col] :
                return
            
            visited[row][col] = True
            
            grid[row][col].isPath = True
            
            
            # draw path to screen 
            #pygame.draw.rect(scr, (0, 120, 0), [grid[row][col].sqx, grid[row][col].sqy, self.sqWidth-1, self.sqWidth-1])
            # time.sleep(.001)
            # pygame.display.update()
            
            time.sleep(.001)
            pygame.event.get()
            pygame.draw.rect(scr, (143, 126, 191), [grid[row][col].sqx, grid[row][col].sqy, self.sqWidth-1, self.sqWidth-1])
            pygame.display.update()
            
            
            # up
            self.DFSAlgo(row-1, col, dest, grid, visited, scr)
            
            # down
            self.DFSAlgo(row+1, col, dest, grid, visited, scr)
            # left

            self.DFSAlgo(row, col-1, dest, grid, visited, scr)
            # right

            self.DFSAlgo(row, col+1, dest, grid, visited, scr)
        

            
        
   
    
    