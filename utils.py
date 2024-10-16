import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import random

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

def dot(x):
    result=0
    for i in range(len(x)):
        result+=x[i]
    return result


def dot(x, y):
    if(len(x)==len(y)):
        result=0
        for i in range(len(x)):
            result+=x[i]*y[i]
        return result
    else:
        print(f"Incompatible dot product between {x} and {y}!")
        return None


def random_unit_circle():
    while True:
        res = np.array((random.random()-0.5, random.random()-0.5))
        if length_sqr(res)<1:
            return res
        

def random_unit_sphere():
    while True:
        res = np.array((random.random()-0.5, random.random()-0.5, random.random()-0.5))
        if length_sqr(res)<1:
            return res


def random_unit_sphere_dir():
    return normalize(random_unit_sphere())


def random_on_hemisphere(normal):
    dir=random_unit_sphere_dir()
    if(dot(dir, normal))>0:
        return dir
    else:
        return -dir


def random_unit_square():
    return np.array((random.random()-0.5, random.random()-0.5))