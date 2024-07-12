from ray import Ray

class HitResult:

    def __init__(self, point, normal=(0,0,0), t=0, front_face=True):
        self.point = point
        self.normal = normal
        self.t=t
        self.front_face = front_face


class Hittable:

    def __init__(self, origin):
        self.origin = origin

    def hit(self, ray: Ray) -> HitResult:
        return None
    

class HittableList:

    def __init__(self, objects=[]):
        self.objects=objects

    def hit(self, ray: Ray, t_min=0, t_max=100000) -> HitResult:

        closest = t_max
        hit_result = None

        for object in self.objects:
            hit = object.hit(ray, t_min, closest)

            if hit!=None:
                closest = hit.t
                hit_result = hit
        
        return hit_result
    
    def add(self, object: Hittable):
        self.objects.append(object)
