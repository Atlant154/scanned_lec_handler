import numpy as np
import os
from PIL import Image

SUCCESS = '\033[92m' + "[Success]" + '\033[0m'
INFO = '\033[94m' + "[Info]" + '\033[0m'
WARNING = '\033[93m' + "[Warning]" + '\033[0m'
ERROR = '\033[91m' + "[Error]" + '\033[0m'

image_ext = [".png", ".jpg", "jpeg"]


def get_image_list(dir):
    dir_files = [f for f in os.listdir(dir) if os.path.isfile(f)]
    result = np.array([])
    try:
        for filename in dir_files:
            if filename.endswith(tuple(image_ext)):
                result = np.append(result, filename)
    except result.size == 0:
        print(ERROR + "There are not matching files in the directory!")
        exit(1)
    else:
        print(INFO + "Scan complete. There are " + str(len(result)) + " matching files in the directory.")
        return result


def create_directory(path):
    try:
        os.mkdir(path)
    except OSError:
        print(ERROR + "Creation of the service directory failed!")
        exit(1)
    else:
        print(INFO + "Service directory was created!")


def delete_directory(path):
    try:
        os.rmdir(path)
    except OSError:
        print(ERROR + "Deletion of the service directory failed!")
        exit(1)
    else:
        print(INFO + "The service directory successfully deleted!")


def is_valid_greeting(greeting_num, image):
    try:
        greeting_num = int(greeting_num)
    except:
        raise ValueError("Number of slice couldn't be cast to integer!")

    im_w, im_h = image.size

    try:
        im_h < greeting_num
    except:
        raise AssertionError("Number of greeting more than image resolution!")

    return True


def slice(image, greeting, save_path="./", save=False):
    im = Image.open(image)

    is_valid_greeting(greeting, im)

