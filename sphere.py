from hittable import Hittable
from ray import Ray
import utils

class Sphere(Hittable):

    def __init__(self, origin, radius):
        self.origin = origin
        self.radius = radius
        super()

    #This calculation is derived from the intersection of the equation of the sphere and the equation of a line in 3D in parametric form
    def hit(self, ray: Ray):
        oc = self.origin - ray.origin
        a = utils.dot(ray.direction, ray.direction)
        b = -2.0 * utils.dot(ray.direction, oc)
        c = utils.dot(oc, oc) - self.radius*self.radius
        discrimant = b*b-4*a*c
        
        if discrimant >= 0:
            return True
        else:
            return False
