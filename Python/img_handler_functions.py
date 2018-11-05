from PIL import ImageEnhance as ench
from PIL import Image
import img2pdf
import zipfile
import shutil
import math
import os

SUCCESS = '\033[92m' + "[Success]" + '\033[0m'
INFO = '\033[94m' + "[Info]" + '\033[0m'
WARNING = '\033[93m' + "[Warning]" + '\033[0m'
ERROR = '\033[91m' + "[Error]" + '\033[0m'

image_ext = [".png", ".jpg", "jpeg"]


def script_init():
    print(INFO + "Supported formats: " + str(image_ext))
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
        print(SUCCESS + "Scan complete. There are " + str(len(result)) + " matching files in the directory.")
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
        print(SUCCESS + "Service directory was created!")


def delete_directory(path):
    try:
        shutil.rmtree(path, ignore_errors=True)
    except OSError:
        print(ERROR + "Deletion of the service directory failed!")
        exit(1)
    else:
        print(SUCCESS + "The service directory successfully deleted!")


def enhance(image, contrast=2.0, color=0.0, brightness=1.0, shape=2.0):
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
        enhanced.filename = image.filename
    except:
        print(ERROR + "Enhance error!")
        shutil.rmtree("./TMP", ignore_errors=True)
        exit(1)
    else:
        image.close()
        return enhanced


def wite_image(image, path):
    filename = image.filename
    filename = filename.split('/')
    filename = filename[-1]
    image.save(path + "/" + filename, "PNG")
    image.close()
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
    archive_name = 'image_archive.zip'
    images = [f for f in os.listdir(path) if os.path.isfile(f) and f.endswith(tuple(image_ext))]
    print(INFO + "Start creating archive!")
    try:
        source_arcive = zipfile.ZipFile(archive_name, 'w')
        for image in images:
            source_arcive.write(image)
        source_arcive.close()
    except:
        print(ERROR + "Creating archive error!")
        os.remove(path + archive_name)
        exit(1)
    else:
        print(SUCCESS + "Sources compressed. Files: " + str(len(images)) + ".")


def remove_sources(path):
    images = [path + f for f in os.listdir(path) if os.path.isfile(f) and f.endswith(tuple(image_ext))]
    print(INFO + "Start deleting sources!")
    try:
        for image in images:
            os.remove(image)
    except:
        print(ERROR + "Removing sources error!")
    else:
        print(SUCCESS + "Sources removed. Files: " + str(len(images)) + ".")


def get_scanline_median(scanline, number):
    n = len(scanline)
    mid = 0.0
    for iter in scanline:
        (R, G, B) = iter
        mid += (R + G + B)

    mid = float(mid) / n
    return (float(mid), number)


def slice_image(image, path, slice_umber=2):
    deviation_coefficient = 0.2

    wight, height = image.size

    if height <= slice_umber:
        print(ERROR + "Image height greater than slice number!")
        return None

    h = math.ceil(height / slice_umber)

    deviation = int(h * deviation_coefficient)

    up = 0
    right = wight
    left = 0

    pixel_matrix = image.load()

    for iter in range(0, math.ceil(slice_umber + slice_umber * deviation_coefficient)):
        scanlines = []
        if up + h + deviation < height:
            for row in range(up + h - deviation, up + h + deviation):
                tempy = [pixel_matrix[column_iter, row] for column_iter in range(left, right)]
                scanlines.append(get_scanline_median(tempy, row))

            max_scanline = max(scanlines, key=lambda item: item[0])[1]
            bottom = up + max_scanline
        else:
            bottom = height

        result_image = image.crop((left, up, right, bottom))
        result_image.filename = "cropped_" + image.filename[2:-4] + "_" + str(iter) + ".png"
        wite_image(image=result_image, path=path)
        result_image.close()
        up = bottom
        if up >= height:
            break

    image.close()
