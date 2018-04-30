"""
Utility functions to be used when training the model
"""
from keras.preprocessing import image
import PIL
import numpy as np
import os


def load_camera_image(img_filename, threshold=80):
    """Preprocesses and loads a camera image

    Notes
    -----
    I found that thresholding the pixels to binary values made the predictor more likely to work which makes sense
    because the generated images only contain binary pixel values

    Parameters
    ----------
    img_filename: str
        Filename of image

    threshold : int
        Cutoff for 0 or 255 pixel value depending on input pixel values


    Returns
    -------
    vectorized_image : np.array
        numpy array representing image pixel values
    """

    img = PIL.Image.open(img_filename, 'r')
    bit_img = img.convert('L')
    bit_img = bit_img.resize((270, 270), resample=PIL.Image.LANCZOS)

    # Thresholding value
    x = image.img_to_array(bit_img)
    x[x > threshold] = 255
    x[x <= threshold] = 0

    return np.expand_dims(x, axis=0)


def load_image(img_filename):
    """Takes an image filename and returns it as a tensor

    Parameters
    ----------
    img_filename: str

    Returns
    -------
    vectorized_image : np.array
        numpy array representing image pixel values
    """
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

