from PIL import ImageEnhance as ench
from PIL import Image
import img2pdf
import zipfile
import shutil
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


def enchance(image, contrast=2.0, color=0.0, brightness=1.0, shape=2.0):
    try:
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
    except:
        print(ERROR + "Enhance error!")
        shutil.rmtree("./TMP", ignore_errors=True)
        exit(1)
    else:
        return enhanced


def wite_image(image, number, path):
    image.save(path + "/" + "scan_" + str(number) + ".png", "PNG")
    return image


def create_pdf(sources_path, result_path):
    print(INFO + "Start generating PDF!")
    pdf_bytes = img2pdf.convert([sources_path + "/" + i for i in os.listdir(sources_path) if i.endswith(".png")])
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
