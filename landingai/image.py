"""
All methods required to make the test and train images for the
classifier
"""

from random import randint, sample, choice
import os
import string

from PIL import Image, ImageFont, ImageDraw

CHARACTERS = string.ascii_letters + "+=:)"
FONT_DIR = os.path.join(os.path.dirname(__file__), "font")


def gen_image(img_name, path, text, font="FreeMono.ttf"):
    """Generates random image with given text"""
    size = (500, 500)
    img = Image.new('1', size, color=1)
    
    # Font left as argument in case user wants to make classification harder
    font_path = os.path.join(FONT_DIR, font)
    fnt = ImageFont.truetype(font_path, 60)

    d = ImageDraw.Draw(img)
    d.text((10, 10), text, font=fnt)
    img.save(os.path.join(path, img_name))
    return


def gen_class():
    """Generates attributes required to images and class label"""
    class_label = randint(0, 1)
    
    if class_label == 0:
        # Add a happy face at the end randomly to make this more difficult
        text = "".join(sample(CHARACTERS, 8)) + choice(["", ":)"])
        return class_label, text
       
    return class_label, "Landing.ai + Ravin Kumar = :)"


def gen_images(train_examples=50, test_examples=10, delete=False):
    """Generates N number of training samples of each class"""
    
    img_name = "class_{0}_imgnum_{1}.bmp"
    for path, n_img in zip(("train", "test"), (train_examples, test_examples)):
        make_images = check_path(path, delete)

        if make_images is True:
            for i in range(n_img):
                class_label, text = gen_class()
                name = img_name.format(class_label, i)
                gen_image(name, path, text)
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
        return True

    os.makedirs(dir_name)
    return True
