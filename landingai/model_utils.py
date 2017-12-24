"""
Utility functions to be used when training the model
"""
from keras.preprocessing import image
import numpy as np
import os


def load_image(img_filename):
    """Takes an image and loads it as a tensor"""
    img = image.load_img(img_filename, grayscale=True, target_size=(270, 270))
    x = image.img_to_array(img)
    return np.expand_dims(x, axis=0)


def class_label(img_filename):
    """Given an image path return class label"""
    return int(img_filename[6])


def load_data(path):
    """Takes path and returns tensor and class labels

    Parameters
    ----------
    path: str
        Name of path that contains images

    Returns
    -------
        array: numpy array
            Tensors that reprsent input image
        targets :
            Two column vector for class prediction
    """
    img_files = os.listdir(path)

    # Load images and convert to 1 bit bitmap
    imgs = np.vstack([load_image(os.path.join(path, img)) for img in img_files])/255
    targets = [class_label(img) for img in img_files]
    return imgs, targets
