import math
from queue import PriorityQueue
import pygame

def reconstructPath(path,current, draw):
    while current in path:
            current = path[current]
            current.makePath()
            draw()

def heuristic(point1,point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1-x2) + abs(y1-y2)

def aStarAlgorithm(draw,grid,start,end):

    count = 0
    openSet = PriorityQueue()
    # This dictinary will keep track of your path
    path = {}
    # add the fScore, count and node into queue
    openSet.put((0,count,start))

    # we are assigning a gScore of infinity for very node in the grid,
    # we are using list comprehension to do this
    gScore = {node: float('inf') for row in grid for node in row }
    gScore[start] = 0

    fScore = {node: float('inf') for row in grid for node in row }
    # we want to know how far the start node is from the end node
    fScore[start] = heuristic(start.getPos(), end.getPos())

    # it check if something is in the priority queue, can't check in the priorityQueue hence
    openSetHash = {start}

    while not openSet.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        # we the get the node that has the lowest fScore,
        # if two nodes have same fScore then we look at count
        current = openSet.get()[2]
        openSetHash.remove(current)
        if( current == end):
            reconstructPath(path,current,draw)
            end.makeEnd()
            return True
            
        for neighbour in current.neighbours:
            tempGScore = gScore[current] + 1
            if tempGScore < gScore[neighbour]:
                # saying we came from neighbour to current
                path[neighbour] = current
                gScore[neighbour] = tempGScore
                fScore[neighbour] = gScore[neighbour] + heuristic(neighbour.getPos(),end.getPos())
                if neighbour not in openSetHash:
                    count += 1
                    openSet.put((fScore[neighbour],count, neighbour))
                    openSetHash.add(neighbour)
                    neighbour.makeOpen()
        
        draw()
        if current != start:
            current.makeClosed()
    
    return False




