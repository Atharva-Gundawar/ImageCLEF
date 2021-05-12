import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
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

def return_prediction(image):

    np.set_printoptions(suppress=True)

    # Loading the model
    model = tensorflow.keras.models.load_model('/content/keras_model.h5')

    # Input data array for the model
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    #resize the image to a 224x224 with the same strategy as in TM2:
    #resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    #turn the image into a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    normalized_image_array = np.stack((normalized_image_array,)*3, axis=-1) # converting gray scale image to 3 channel image
    
    # Adding the image to the 
    data[0] = normalized_image_array
    start_time = time.time()
    prediction = model.predict(data)
    time_req_pred = time.time() - start_time
    print(labels[np.argmax(prediction[0])])
    return prediction[0],time_req_pred
