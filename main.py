import pygame
import math
from node import Node
import constants
from astar import aStarAlgorithm
from DFS import depthFirstSearch
from BFS import breathFirstSearch

# Setting up the display window 
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption("Pathfinding Visulaizer")


def createGrid(rows,width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node =  Node(i,j,gap,rows)
            grid[i].append(node)
    
    return grid

def drawGrid(win,rows,width):
    gap = width // rows
    for i in range(rows):
        # I'm creating a line for each row
        pygame.draw.line(win,constants.GREY,(0,i * gap),(width, i *gap))
        for j in range(rows):
            # I'm creating a line for each colum
            pygame.draw.line(win,constants.GREY,(j * gap,0),(j*gap, width))

def draw(win,grid,rows,width):
    win.fill(constants.LIGHTGREY)

    #looping through all the spots in the grid and actually drawing them
    for row in grid:
        for node in row:
            node.draw(win)
    
    #drawing the grid lines on top
    drawGrid(win,rows,width)

    #tells pygame to update the display
    pygame.display.update()

def getClickedPos(pos,rows,width):
    gap = width // rows
    y, x = pos
    
    row = y // gap
    col = x // gap

    return row, col

def main(win, width):

    ROWS = 50
    grid = createGrid(ROWS,width)
    
    start = None
    end = None

    run = True
    started = False

    while run:
        draw(win,grid,ROWS,width)
        # we are looping through every event that has happened in the pygame
        #Pygame will register all the events from the user into an event 
        # queue which can be received with the code pygame.event.get()
        for event in pygame.event.get():
            # if we press the exit button on the screen stop running the game
            if event.type == pygame.QUIT:
                run = False
            

            #if left mouse button pressed
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                # gets spot clicked on from the 2d list
                row, col = getClickedPos(pos, ROWS, width)
                node = grid[row][col]
                if not start and node != end:
                    start = node
                    #create start node
                    start.makeStart()
                elif not end and node != start :
                    end = node
                    #create end node
                    end.makeEnd()
                elif node != end and start:
                    #create walls
                    node.makeBarrier()
                 
            #if right mouse button pressed
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = getClickedPos(pos, ROWS, width)
                node = grid[row][col]
                node.reset()
                if node == start:
                    start = None
                if node == end:
                    end = None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and start and end:
                    for row in grid:
                        for node in row:
                            node.updateNeighbours(grid)
                            #lambda is a anonymous function
                    aStarAlgorithm(lambda: draw(win, grid, ROWS, width),grid, start, end)
                
                if event.key == pygame.K_d and start and end:
                    for row in grid:
                        for node in row:
                            node.updateNeighbours(grid)
                    
                    depthFirstSearch(lambda: draw(win,grid, ROWS, width), grid, start, end)

                if event.key == pygame.K_b and start and end:
                    for row in grid:
                        for node in row:
                            node.updateNeighbours(grid)
                    
                    breathFirstSearch(lambda: draw(win,grid, ROWS, width), grid, start, end)
                    
                
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = createGrid(ROWS, width)


    pygame.quit()

main(WIN,WIDTH)
