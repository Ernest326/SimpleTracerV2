from ray import Ray

class HitResult:

    def __init__(self, point, normal):
        self.point = point
        self.normal = normal


class Hittable:

    def __init__(self, origin):
        self.origin = origin

    def hit(self, ray: Ray) -> HitResult:
        return None