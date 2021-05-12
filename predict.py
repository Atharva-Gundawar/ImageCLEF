import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
from google.colab.patches import cv2_imshow
import warnings
import time

def get_labels():
    with open('/content/labels.txt','r') as f:
        content = f.readlines()
    content = [x.strip() for x in content] 

    labels = {}

    for x in content:
        index,label = x.split(' ')
        labels[int(index)] = label

    return labels 

