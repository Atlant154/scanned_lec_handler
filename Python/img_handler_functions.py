from PIL import ImageEnhance as ench
from PIL import Image
import shutil
import img2pdf
import os

SUCCESS = '\033[92m' + "[Success]" + '\033[0m'
INFO = '\033[94m' + "[Info]" + '\033[0m'
WARNING = '\033[93m' + "[Warning]" + '\033[0m'
ERROR = '\033[91m' + "[Error]" + '\033[0m'

image_ext = [".png", ".jpg", "jpeg"]


def get_image_list(dir):
    dir_files = [f for f in os.listdir(dir) if os.path.isfile(f)]
    result = []
    try:
        for filename in dir_files:
            if filename.endswith(tuple(image_ext)):
                result.append(Image.open(filename))
    except result == 0:
        print(ERROR + "There are not matching files in the directory!")
        exit(1)
    else:
        print(INFO + "Scan complete. There are " + str(len(result)) + " matching files in the directory.")
        return result


def create_directory(path):
    try:
        if not os.path.exists(path):
            os.mkdir(path)
    except OSError:
        print(ERROR + "Creation of the service directory failed!")
        exit(1)
    else:
        print(INFO + "Service directory was created!")


def delete_directory(path):
    try:
        shutil.rmtree(path, ignore_errors=True)
    except OSError:
        print(ERROR + "Deletion of the service directory failed!")
        exit(1)
    else:
        print(INFO + "The service directory successfully deleted!")


def enchance(image, percent):
    coeff = (percent / 100.0) + 1.0
    enchancer = ench.Contrast(image)
    enh = enchancer.enhance(coeff)
    return enh


def wite_image(image, number, path):
    image.save(path + "/" + "scan_" + str(number) + ".png", "PNG")
    return image


def create_pdf(sources_path, result_path):
    pdf_bytes = img2pdf.convert([sources_path + "/" + i for i in os.listdir(sources_path) if i.endswith(".png")])
    result_file = open(result_path + "/uncompressed.pdf", "wb")
    result_file.write(pdf_bytes)
