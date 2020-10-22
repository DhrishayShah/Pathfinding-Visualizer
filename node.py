import constants
import pygame

class Node:
    def __init__(self, row, col, width, totalRows):
        self.row = row
        self.col = col
        #coordinate positions of each node
        self.x = row * width
        self.y = col * width

        self.colour = constants.LIGHTGREY
        self.neighbours = []
        self.width = width
        self.totalRows = totalRows
    
    def getPos(self):
        return self.row, self.col

    # returns true if the colour is colur is right
    def isClosed(self):
        return self.colour == constants.RED

    def isOpen(self):
        return self.colour == constants.GREEN
    
    def isBarrier(self):
        return self.colour == constants.BLACK

    def isStart(self):
        return self.colour == constants.ORANGE

    def isEnd(self):
        return self.colour == constants.TURQUOISE

    #setting the colour of the squares depending on state of the square
    def reset(self):
        self.colour = constants.WHITE

    def makeStart(self):
        self.colour = constants.ORANGE
    
    def makeClosed(self):
        self.colour = constants.RED

    def makeOpen(self):
        self.colour = constants.GREEN

    def makeBarrier(self):
        self.colour = constants.BLACK

    def makeEnd(self):
        self.colour = constants.TURQUOISE
    
    def makePath(self):
        self.colour = constants.YELLOW

    
    #this method is used to draw a sqaure
    def draw(self,win):
        pygame.draw.rect(win,self.colour,(self.x,self.y,self.width,self.width))

    def updateNeighbours(self,grid):
        self.neighbours = []

        # check if the positon at the bottom is not a barrier, if not add to neighbours list
        if self.row < self.totalRows - 1 and not grid[self.row + 1][self.col].isBarrier():
            self.neighbours.append(grid[self.row + 1][self.col])
        
        # check if the position above is not a barrier, if not add to neighbours list
        if self.row > 0 and not grid[self.row - 1][self.col].isBarrier():
            self.neighbours.append(grid[self.row - 1][self.col])
        
        # check if the position on the right is not a barrier, if not add to neigbours list
        if self.col < self.totalRows - 1 and not grid[self.row][self.col + 1].isBarrier():
            self.neighbours.append(grid[self.row][self.col + 1])
        
        # check if the positon on the left is not a barrier, if not add to neigbours list
        if self.col > 0 and not grid[self.row][self.col - 1].isBarrier():
            self.neighbours.append(grid[self.row][self.col - 1])

    #this stands for less than, used to compare two node objects
    def __lt__(self,other):
        return False



