import pygame
import numpy as np

class Square():
    def __init__(self, row, col, sqx, sqy, width):
        self.row = row
        self.col = col
        
        self.sqx = sqx
        self.sqy = sqy
        self.width = width
        
        self.isWall = False
        self.isPath = False
        self.isVisited = False
        self.isMazeVisited = False
       
        self.isStartNode = False
        self.isEndNode = False
        self.isPickedUp = False
        
        self.prevTile = None
        self.dist = np.inf
        
    def hover(self, pos, win):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.sqx and pos[0] < self.sqx + self.width:
            if pos[1] > self.sqy and pos[1] < self.sqy + self.width:
                #print("BUTTON HOVERED")
                pygame.draw.rect(win, (13, 255, 0), [self.sqx, self.sqy, self.width-1, self.width-1 ])# x    y    width     height
                pygame.display.update()
                # pygame.draw.rect(win, (192, 192, 192), (self.sqx, self.sqy, 4, self.width), 0)                
                # pygame.draw.rect(win, (192, 192, 192), (self.sqx, self.sqy+self.width-4, self.width, 4),0)
                # pygame.draw.rect(win, (192, 192, 192), (self.sqx,self.sqy,self.width, 4), 0)
                # pygame.draw.rect(win, (192, 192, 192), (self.sqx+self.width-4, self.sqy, 4 ,self.width),0)
                #print(self.row, self.col, " IS BEING HOVERED")
                
                #pygame.draw.rect(win, (192, 192, 192), (self.x-2,self.y-2,self.width+4,self.height+4),0)
                return True    
        return False
    