import numpy as np
import pygame 
import time

class Dijkstra:

    
    def __init__(self, grid, start, dest, GRID_HEIGHT, GRID_WIDTH, sqWidth, scr):
        self.boardHeight = GRID_HEIGHT
        self.boardWidth = GRID_WIDTH
        self.sqWidth = sqWidth
        self.start = start
        self.dest = dest
        
        
        visitedInOrder = self.dijkstraAlgo(grid, start, dest, scr, self.boardWidth, self.boardHeight)
        
        for tile in reversed(visitedInOrder):
              #print the visual board thing here
            time.sleep(.005)
            pygame.event.get()
            pygame.draw.rect(scr, (143, 126, 191), [grid[tile.row][tile.col].sqx, grid[tile.row][tile.col].sqy, self.sqWidth-1, self.sqWidth-1])
            pygame.display.update()
        
        self.showFinalPath(grid, dest, scr)
        
    
        
    def showFinalPath(self, grid, dest, scr):
        
        
        reversedpath = []
        head = grid[dest[0]][dest[1]]
         
        while head.prevTile != None:
            head.isPath = True
            reversedpath.insert(0, head)
            head = head.prevTile
        
        for tile in reversedpath:
            pygame.event.get()
            time.sleep(.02)
            pygame.draw.rect(scr, (245, 164, 66), [grid[tile.row][tile.col].sqx, grid[tile.row][tile.col].sqy, self.sqWidth-1, self.sqWidth-1])
            pygame.display.flip()
            
    def getAllTiles(self,grid, width, height):
        tiles = []
        for i in range(0, width):
            for j in range(0, height):
                print(i)
                print(j)
                if not grid[i][j].isWall:
                   
                    tiles.insert(0, (grid[i][j]))
        print("all tiles", tiles)
        return tiles
    
    def getUnvisitedNeighbors(self, grid, tile, width, height):
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
        
        
    def updateUnvisitedNeighbors(self, grid, tile, width, height):
        unvisited = self.getUnvisitedNeighbors(grid, tile, width, height)
        
        for neighbor in unvisited:
            neighbor.dist = tile.dist + 1
            neighbor.prevTile = tile # for backtracking visual
    
    
    def dijkstraAlgo(self, grid, start, dest, scr, width, height):
        
        print("dijkstraAlgo is running")
        visitedTilesInOrder = []
        
        grid[start[0]][start[1]].dist = 0
        
        unvisitedTiles = self.getAllTiles(grid, width, height)
        
        while len(unvisitedTiles) > 0:
            
            unvisitedTiles.sort(key=lambda x: x.dist)
            
            closestTile = unvisitedTiles.pop(0)
            
            if (closestTile.dist == np.inf):
                return visitedTilesInOrder
            
            if closestTile.dist != np.inf:
                closestTile.isVisited = True
                visitedTilesInOrder.insert(0, closestTile)
            
            if (closestTile.isEndNode):
                print("FOUND THE DESTINATION")
                return visitedTilesInOrder
            
              #print the visual board thing here
            # time.sleep(.02)
            # pygame.event.get()
            # pygame.draw.rect(scr, (143, 126, 191), [grid[closestTile.row][closestTile.col].sqx, grid[closestTile.row][closestTile.col].sqy, self.sqWidth-1, self.sqWidth-1])
            # pygame.display.update()
            
            self.updateUnvisitedNeighbors(grid, closestTile, width, height)
            
        



