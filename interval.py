import numpy as np

class interval:

    def __init__(self, min=np.inf, max=-np.inf):
        self.min= min
        self.max = max

    def contains(self, x):
        return (x<=self.max and x>=self.min)
    
    def surrounds(self, x):
        return (x<self.max and x>self.min)
    
    def size(self):
        return self.max-self.min

    
universe = interval(-np.inf, np.inf)
empty = interval()