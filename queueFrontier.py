from stack import StackFrontier
class QueueFrontier(StackFrontier):
    
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node