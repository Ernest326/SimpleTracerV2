from hittable import Hittable, HitResult
from ray import Ray
import numpy as np
import utils

class Sphere(Hittable):

    def __init__(self, origin, radius):
        self.origin = origin
        self.radius = radius
        super()

    #This calculation is derived from the intersection of the equation of the sphere and the equation of a line in 3D in parametric form
    #The calculations are then further simplified to give us this monstrosity
    def hit(self, ray: Ray):

        #-b formula bullshit
        oc = self.origin - ray.origin
        a = utils.dot(ray.direction, ray.direction)
        h = utils.dot(ray.direction, oc)
        c = utils.length_sqr(oc) - self.radius*self.radius

        #Discriminant checks if there is at least one valid solution
        discriminant = h*h - a*c

        #P=Q+td, here we are getting t, the variable for distance along direction
        t = (h-np.sqrt(discriminant) ) / a;
        
        #If we dont hit or object is behind us
        if discriminant<0 or t<0:
            return None
        else:
            point = ray.at(t)
            normal = utils.normalize(self.origin - point)
            return HitResult(point, normal)
