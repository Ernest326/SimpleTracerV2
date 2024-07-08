import numpy as np

class Ray:

    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def magnitude(self):
        return np.sqrt(self.direction.dot(self.direction))
    
    def at(self, t):
        return self.origin + self.direction*t