from ray import Ray
import utils
import numpy as np

WIDTH = 1024
HEIGHT = 720
ASPECT_RATIO = float(WIDTH)/float(HEIGHT)

CAMERA_ORIGIN = np.array([0, 0, 0])
FOCAL_LENGTH = 1

VIEWPORT_HEIGHT = 2.0
VIEWPORT_WIDTH = VIEWPORT_HEIGHT/ASPECT_RATIO

SAMPLE_COUNT = 200
LIGHT_BOUNCES = 15

image = utils.gradient(WIDTH, HEIGHT, [255, 255, 255], [100, 100, 180])

if __name__ == "__main__":

    for v in range(HEIGHT):
        for u in range(WIDTH):

            uv_vp = np.array([VIEWPORT_WIDTH, VIEWPORT_HEIGHT])*np.array([u/WIDTH, v/WIDTH])
            vp_coord = np.array([uv_vp[0], uv_vp[1], 0]) - [VIEWPORT_WIDTH/2, VIEWPORT_HEIGHT, -FOCAL_LENGTH]

            image[v][u]=[(uv_vp[0]/VIEWPORT_WIDTH)*255, (uv_vp[1]/VIEWPORT_HEIGHT)*255, 0]

    utils.save_image(image)
    utils.display_image(image)