import pygame

class Button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        #print("BUTTON SET UP!")

    def draw(self,win,outline=None):
        #print("BUTTON BEING DRAWN")
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 10)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
   
        
    def hover(self, pos, win):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                #print("BUTTON HOVERED")                    # x    y    width     height
                pygame.draw.rect(win, (192, 192, 192), (self.x, self.y, 4, self.height), 0)                
                pygame.draw.rect(win, (192, 192, 192), (self.x, self.y+self.height-4, self.width, 4),0)
                pygame.draw.rect(win, (192, 192, 192), (self.x,self.y,self.width, 4), 0)
                pygame.draw.rect(win, (192, 192, 192), (self.x+self.width-4, self.y, 4 ,self.height),0)
                
                #pygame.draw.rect(win, (192, 192, 192), (self.x-2,self.y-2,self.width+4,self.height+4),0)
                return True    
        return False