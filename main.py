from ray import Ray
import utils
import numpy as np
from sphere import Sphere
import time

WIDTH = 400
ASPECT_RATIO = 16.0/9.0
HEIGHT = max(1,int(WIDTH/ASPECT_RATIO))

CAMERA_ORIGIN = np.array([0, 0, 0])
FOCAL_LENGTH = 1

VIEWPORT_HEIGHT = 2.0
VIEWPORT_WIDTH = VIEWPORT_HEIGHT*float(WIDTH)/HEIGHT

SAMPLE_COUNT = 200
LIGHT_BOUNCES = 15

image = utils.gradient(WIDTH, HEIGHT, [255, 255, 255], [100, 100, 180])

sphere = Sphere((0,0,1), 0.5)

if __name__ == "__main__":

    start_time = time.time()

    du = VIEWPORT_WIDTH/WIDTH
    dv = VIEWPORT_HEIGHT/HEIGHT
    top_left = np.array([-VIEWPORT_WIDTH/2, -VIEWPORT_HEIGHT/2, FOCAL_LENGTH])
    pixel0 = top_left + 0.5*np.array((du, dv, 0))

    for v in range(HEIGHT):
        for u in range(WIDTH):

            #Every n pixels output progress
            if(v*WIDTH+u)%20==0:
               print(f"Progress: {v*WIDTH+u}/{WIDTH*HEIGHT}\t[{((v*WIDTH+u)/(WIDTH*HEIGHT))*100:.2f}]")

            pixel_coord = pixel0 + np.array([u*du,v*dv,0])
            ray_dir = pixel_coord-CAMERA_ORIGIN #It doesnt matter whether direction is normalized or not
            #ray_dir = utils.normalize(pixel_coord-CAMERA_ORIGIN)

            ray = Ray(CAMERA_ORIGIN, ray_dir)
            hit = sphere.hit(ray)

            if (hit != None):
                image[v][u]=np.array((hit.normal[0]+1, hit.normal[1]+1, hit.normal[2]+1))*0.5*255
            
            #print(utils.normalize(vp_coord))
    print(f"COMPLETE!!!\tTime Taken: {time.time()-start_time:.2f} seconds")

    utils.save_image(image)
    utils.display_image(image)