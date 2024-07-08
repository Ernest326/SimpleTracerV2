import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

def gradient(w, h, c1, c2):

    c1=np.array(c1)
    c2=np.array(c2)

    gradient = np.zeros((h, w, 3), dtype=np.uint8)

    for i in range(h):
        c = c1+(c2-c1)*(i/h)
        for j in range(w):
            gradient[i][j]=c

    return gradient

def display_image(image):
    plt.imshow(image, interpolation='nearest')
    plt.show()


def save_image(image):
    img = Image.fromarray(image)
    img.save("output.jpg")


def length(arr):
    mag=0
    for i in arr:
        mag+=i*i
    mag=np.sqrt(mag)
    return mag


def length_sqr(arr):
    mag=0
    for i in arr:
        mag+=i*i
    return mag


def normalize(arr):
    return arr/length(arr)


def dot(x, y):
    if(len(x)==len(y)):
        result=0
        for i in range(len(x)):
            result+=x[i]*y[i]
        return result
    else:
        print(f"Incompatible dot product between {x} and {y}!")
        return None