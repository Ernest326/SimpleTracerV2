from hittable import Hittable
from ray import Ray

class Sphere(Hittable):

    def __init__(self):
        super()

    def hit(self, ray: Ray):
        dir = ray.origin - self.origin
        a = ray.mag()
        #half_b = 
        return None
