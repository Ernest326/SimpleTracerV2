import numpy as np

class Ray:

    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def magnitude(self):
        return np.sqrt(self.direction.dot(self.direction))