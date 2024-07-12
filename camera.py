import numpy as np
from ray import Ray
from hittable import HittableList
from interval import interval
import utils

class Camera:

    def __init__(self, position=np.array((0,0,0)), rotation=np.array((0,0,0))):

        #Quality Settings
        self.samples = 200
        self.max_bounces = 10

        self.near = 0
        self.far = np.inf

        #Image Settings
        self.focal_length = 1.0

        self.aspect_ratio = 16/9
        self.image_width = 400
        self.image_height = int(self.image_width/self.aspect_ratio)

        self.viewport_height = 2.0
        self.viewport_width = self.viewport_height * (float(self.image_width)/self.image_height)

        #Positional settings
        self.position = position
        self.rotation = rotation

        self.show_progress = True


    def ray_color(self, ray, world: HittableList):

        hit= world.hit(ray, interval(self.near, self.far))

        if hit!=None:
            return np.array((hit.normal[0]+1, hit.normal[1]+1, hit.normal[2]+1))*0.5*255
        else:
            a = (utils.normalize(ray.direction)[1]+1)*0.5
            return (1-a)*np.array((255, 255, 255)) + a*np.array((80, 80, 150))


    def render(self, world: HittableList):
        
        image = np.zeros((self.image_height, self.image_width, 3), dtype=np.uint8)

        du = self.viewport_width/self.image_width
        dv = -self.viewport_height/self.image_height

        top_left = np.array([-self.viewport_width/2, self.viewport_height/2, -self.focal_length])
        pixel0 = top_left + 0.5*np.array((du, dv, 0))

        for v in range(self.image_height):
            for u in range(self.image_width):

                #Every n pixels output progress
                if(v*self.image_width+u)%100==0 and self.show_progress:
                    print(f"Progress: {v*self.image_width+u}/{self.image_width*self.image_height}\t[{((v*self.image_width+u)/(self.image_width*self.image_height))*100:.2f}]")

                pixel_coord = pixel0 + np.array([u*du,v*dv,0])
                ray_dir = pixel_coord-self.position #It doesnt matter whether direction is normalized or not
                #ray_dir = utils.normalize(pixel_coord-CAMERA_ORIGIN)

                ray = Ray(self.position, ray_dir)
                color = self.ray_color(ray, world)

                image[v][u]=color

        return image