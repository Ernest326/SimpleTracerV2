from ray import Ray

class HitResult:

    def __init__(self, point, normal=(0,0,0), color=(0,0,0)):
        self.point = point
        self.normal = normal
        self.color = color


class Hittable:

    def __init__(self, origin):
        self.origin = origin

    def hit(self, ray: Ray) -> HitResult:
        return None