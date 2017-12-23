"""
All methods required to make the test and train images for the
classifier
"""
import shutil
from random import randint, sample, choice
from collections import namedtuple
import os
import string

from PIL import Image, ImageFont, ImageDraw

CHARACTERS = string.ascii_letters + "."
FONT_DIR = os.path.join(os.path.dirname(__file__), "font")
PARAMS_C = namedtuple("params", ["text_size", "rotation", "x", "y"])


def random_params(scale=(95, 100), rotation=(-5, 5), text_x=(60, 100), text_y=(300, 350)):
    """Generates random parameters for sample images

    Parameters
    ----------
    scale: tuple
        Min and Max bounds for text size
    rotation : tuple
        Min and Max rotation bounds for text
    text_x : tuple
        Sets the x for the corner
    text_y : tuple
        Sets the y for the corner


    Returns
    -------
    params: named tuple
        Returns named tuple for use in gen_image
    """
    values = []
    for param_bounds in (scale, rotation, text_x, text_y):
        values.append(choice(range(*param_bounds)))
    return PARAMS_C(*values)


def gen_image(img_name, path, text, params, font="AllertaStencil-Regular.ttf"):
    """Generates random image with given text"""
    base_size = (1080, 1080)
    base_img = Image.new('1', base_size, color=1)

    # Draw text_size, font_size, and spacing found through experimentation
    text_size = (855, 465)
    text_img = Image.new('1', text_size, color=0).convert('RGBA')

    # Add text to image
    font_path = os.path.join(FONT_DIR, font)
    font_size = 110
    fnt = ImageFont.truetype(font_path, font_size)
    d = ImageDraw.Draw(text_img)

    spacing = 30
    d.multiline_text((30, 0), text=text, spacing=spacing, font=fnt, fill="white")

    # Rotate text image and add background
    text_img = text_img.rotate(params.rotation, expand=True)
    fff = Image.new('RGBA', text_img.size, (255,) * 4)
    text_rotation = Image.composite(text_img, fff, text_img)

    # Paste onto image and save
    base_img.paste(text_rotation, (params.x, params.y))
    base_img.save(os.path.join(path, img_name))
    return


def gen_class():
    """Generates attributes required to images and class label"""
    class_label = randint(0, 1)
    template = "{0} +\n{1} = \n{2}"

    if class_label == 0:
        # Add a happy face at the end randomly to make this more difficult
        text_1 = "".join(sample(CHARACTERS, 11)) + choice(["", ":)"])
        text_2 = "".join(sample(CHARACTERS, 11)) + choice(["", ":)"])
        text_3 = choice(["".join(sample(CHARACTERS, 2)), ":)"])
        text = template.format(text_1, text_2, text_3)
        return class_label, text
       
    return class_label, template.format("LANDING.AI", "Ravin Kumar", ":)")


def gen_images(train_examples=50, test_examples=10, delete=False):
    """Generates N number of training samples of each class"""
    img_name = "class_{0}_imgnum_{1}.bmp"

    for path, n_img in zip(("train", "test"), (train_examples, test_examples)):
        make_images = check_path(path, delete)

        if make_images is True:
            for i in range(n_img):

                params = random_params()
                class_label, text = gen_class()
                name = img_name.format(class_label, i)
                gen_image(name, path, text, params)
    return


def check_path(dir_name, delete=False):
    """Check if path exists and optionally deletes. Returns true if 
    images should be created"""

    if os.path.isdir(dir_name) is True and delete is False:
        print(("{0} exists, skipping creation of "
               "directory and image".format(dir_name)))

        return False

    elif os.path.isdir(dir_name) is True and delete is True:
        print(("{0} exists, deleting directory and images "
               "and creating new ones".format(dir_name)))
        shutil.rmtree(dir_name)

    os.makedirs(dir_name)
    return True

