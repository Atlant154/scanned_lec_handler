from PIL import ImageEnhance as ench
from PIL import Image
import img2pdf
import zipfile
import shutil
import math
import gc
import os

SUCCESS = '\033[92m' + "[Success]" + '\033[0m'
INFO = '\033[94m' + "[Info]" + '\033[0m'
WARNING = '\033[93m' + "[Warning]" + '\033[0m'
ERROR = '\033[91m' + "[Error]" + '\033[0m'

image_ext = [".png", ".jpg", "jpeg"]


def script_init():
    print(INFO + "Supported formats: " + str(image_ext));
    print(SUCCESS + "Script is running!")


def get_image_list(dir):
    print(INFO + "Start scanning the directory!")
    dir_files = [f for f in os.listdir(dir) if os.path.isfile(f) and f.endswith(tuple(image_ext))]
    dir_files.sort()
    result = []
    try:
        result = [Image.open(dir + filename) for filename in dir_files]
    except result == 0:
        print(ERROR + "There are not matching files in the directory!")
        exit(1)
    else:
        print(INFO + "Scan complete. There are " + str(len(result)) + " matching files in the directory.")
        return result


def create_directory(path):
    print(INFO + "Start creating service directory!")
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


def enhance(image, contrast=2.0, color=0.0, brightness=1.0, shape=2.0):
    try:
        print(image.filename)
        # Color enhance:
        enhancer = ench.Color(image)
        enhanced = enhancer.enhance(color)
        # Brightness enhance:
        enhancer = ench.Brightness(enhanced)
        enhanced = enhancer.enhance(brightness)
        # Contrast enhance:
        enhancer = ench.Contrast(enhanced)
        enhanced = enhancer.enhance(contrast)
        # Shape enhance:
        enhancer = ench.Sharpness(enhanced)
        enhanced = enhancer.enhance(shape)
        enhanced.filename = image.filename
    except:
        print(ERROR + "Enhance error!")
        shutil.rmtree("./TMP", ignore_errors=True)
        # exit(1)
    else:
        gc.collect()
        return enhanced


def wite_image(image, path):
    image.save(path + "/" + image.filename, "PNG")
    return image


def create_pdf(sources_path, result_path):
    print(INFO + "Start generating PDF!")
    file_list = [sources_path + "/" + i for i in os.listdir(sources_path) if i.endswith(".png")]
    file_list.sort()
    pdf_bytes = img2pdf.convert(file_list)
    result_file = open(result_path + "/uncompressed.pdf", "wb")
    result_file.write(pdf_bytes)
    print(SUCCESS + "Uncompressed PDF created!")


def compress_files(path):
    archive_name = "image_archive.zip"
    print(INFO + "Start creating archive!")
    try:
        archive = zipfile.ZipFile(archive_name, "w")
        for dirname, subdirs, files in os.walk(path):
            for filename in files:
                if filename.endswith(tuple(image_ext)):
                    archive.write(os.path.join(dirname, filename))
    except:
        print(ERROR + "Creating archive error!")
        os.remove("./Images.zip")
    else:
        print(SUCCESS + "Image archive created!")
        print(INFO + "Start deleting images")
        try:
            list_dir = os.listdir(path)
            for file in list_dir:
                if file.endswith(tuple(image_ext)):
                    os.remove(os.path.join(path, file))
        except:
            print(ERROR + "Images removing error!")
        else:
            print(SUCCESS + "Images removed!")

def enum(iter, start=1):
    n = start
    for i in iter:
        yield n, i
        n += 1


def slice_image(image, slice_num=2):
    wight, height = image.size

    upper = 0

    slices = int(math.ceil(height / slice_num))

    for i,slice in enum(range(slice_num)):
        left = 0;
        upper = upper
        if i == slice_num:
            lower = height
        else:
            lower = int(i)