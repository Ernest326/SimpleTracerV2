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