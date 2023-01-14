import pygame
import random

class MakePrimsMaze():
    
    def __init__(self, grid, start, dest, sqwidth, scr):
        self.start = start
        self.dest = dest
        self.sqwidth = sqwidth
        
        self.width = len(grid[0])
        self.height = len(grid)
        
        self.generatePrimsMaze(grid, start, dest, sqwidth, scr)
        
    def getNeighbors(self, grid, tile, width, height):
        neighbors = []
        row = tile.row
        col = tile.col
        # top
        if row-1 >= 0:
            if not grid[row-1][col].isVisited:
                neighbors.insert(0, grid[row-1][col])
        # down
        if row+1 <= width-1:
            if not grid[row+1][col].isVisited:
                neighbors.insert(0, grid[row+1][col])
        # left
        if col-1 >= 0:
            if not grid[row][col-1].isVisited:
                neighbors.insert(0, grid[row][col-1])
        # right
        if col+1 <= height-1:
            if not grid[row][col+1].isVisited:
                neighbors.insert(0, grid[row][col+1])

        return neighbors
        
        
    def generatePrimsMaze(self, grid, start, dest, sqwidth, scr):
        print("Generating prims maze...")
        
        grid[start[0]][start[1]].isMazeVisited = True
        pendingNeighbors = self.getNeighbors(grid, grid[start[0]][start[1]], len(grid[0]), len(grid))
        
        while len(pendingNeighbors) > 0:
            randomNeighbor = random.choice(pendingNeighbors)
            pendingNeighbors.remove(randomNeighbor)
            
            
        
        
        
        allTiles = [] # build  alist of all the possible indices in the grid
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                allTiles.append((i, j))
        
        
        while allTiles:
            randomIndices = random.choice(allTiles)
            allTiles.remove(randomIndices)
        # grid[randomIndices[0]][randomIndices[1]].isWall = False