import time
import utils
from sphere import Sphere
from hittable import HittableList
from camera import Camera

sphere = Sphere((0,0,-1), 0.5)
sphere2 = Sphere((0, -10.5, -1), 10)

world = HittableList()
world.add(sphere)
world.add(sphere2)

main_cam = Camera()


if __name__ == "__main__":

    start_time = time.time()
    image = main_cam.render(world)
    print(f"COMPLETE!!!\tTime Taken: {time.time()-start_time:.2f} seconds")

    utils.save_image(image)
    utils.display_image(image)