from PIL import Image
from matplotlib import pyplot as plt
import numpy as np

WIDTH = 1024
HEIGHT = 720
SAMPLE_COUNT = 200

def gradient(w, h, c1, c2):

    c1=np.array(c1)
    c2=np.array(c2)

    gradient = np.zeros((h, w, 3), dtype=np.uint8)

    for i in range(h):
        c = c1+(c2-c1)*(i/h)
        for j in range(w):
            gradient[i][j]=c

    return gradient


image = gradient(WIDTH, HEIGHT, [255, 255, 255], [100, 100, 180])

def display_image():
    plt.imshow(image, interpolation='nearest')
    plt.show()


def save_image():
    img = image.fromarray(image)
    img.save("output.jpg")


if __name__ == "__main__":
    display_image()