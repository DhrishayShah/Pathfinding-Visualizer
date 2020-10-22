
from stack import StackFrontier
import pygame

def reconstructPath(path,current, draw):
    while current in path:
            current = path[current]
            current.makePath()
            draw()


def depthFirstSearch(draw,grid,start,end):
    
    count = 0
    #This list will be implemented as a stack, first in first out
    stackFrontier = StackFrontier()

    #This dictionary will keep track of the path
    path = {}

    #Initializing an empty explored set
    explored = set()
    #currentCost = {node: float('inf') for row in grid for node in row}
    #currentCost[start] = 0

    totalCost = {node: float('inf') for row in grid for node in row}
    totalCost[start] = 0
    stackFrontier.add((0,count, start))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = stackFrontier.remove()[2]
        
        
        if current == end:
            reconstructPath(path,current,draw)
            end.makeEnd()
            break
        
        explored.add(current)

        for neighbour in current.neighbours:
            tempCost = totalCost[current] + 1
            if tempCost < totalCost[neighbour]:
                path[neighbour] = current
                totalCost[neighbour] = tempCost
                if not stackFrontier.contains(neighbour) and neighbour not in explored  :
                    count += 1
                    stackFrontier.add((totalCost[neighbour], count, neighbour))
                    neighbour.makeOpen()
            
        draw()
        if current != start:
            current.makeClosed()
    
    return True

        
        
    


