from ray import Ray
import utils

WIDTH = 1024
HEIGHT = 720
SAMPLE_COUNT = 200
LIGHT_BOUNCES = 15

image = utils.gradient(WIDTH, HEIGHT, [255, 255, 255], [100, 100, 180])

if __name__ == "__main__":
    utils.save_image(image)
    utils.display_image(image)