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
    #The calculations are then further simplified(b=-2h) to give us this monstrosity
    def hit(self, ray: Ray, t_min=0, t_max=100000):

        #-b formula bullshit
        oc = self.origin - ray.origin
        a = utils.dot(ray.direction, ray.direction)
        h = utils.dot(ray.direction, oc)
        c = utils.length_sqr(oc) - self.radius*self.radius

        #Discriminant checks if there is at least one valid solution
        discriminant = h*h - a*c

        if discriminant < 0:
            return None
        
        sqrtd = np.sqrt(discriminant)
        
        #P=Q+td, here we are getting t, the variable for distance along direction, quadratic formula where -2b=h and discrinimant = b^2-4ac
        root = (h-sqrtd)/a
        if root<=t_min or root>=t_max:
            root = (h+sqrtd)/a
            if root<=t_min or root>=t_max:
                return None

        point = ray.at(root)

        normal = (point-self.origin)/self.radius #Fancy way of normalising without vector length calculation
        front_face = True

        if utils.dot(ray.direction, normal)>0:
            normal = -normal
            front_face = False
        
        return HitResult(point, normal, root, front_face)
