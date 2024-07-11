import numpy as np
import utils

class Ray:

    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def magnitude(self):
        return np.sqrt(utils.dot(self.direction))
    
    def at(self, t):
        return self.origin + self.direction*t