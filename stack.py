#Stack - First in First Out

class StackFrontier():
    def __init__(self):
        # I am using a list to implement a stack
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains(self, neighbour):
        for container in self.frontier:
            for node in container:
                if(node == neighbour):
                    return True
        
        return False


    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            # -1 gets us the last node
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

    