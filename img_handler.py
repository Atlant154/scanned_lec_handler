import src.libImgHandler as imf
import itertools
import os

# Service directory:
tmp = "./TMP"

# Target directory:
path = os.getcwd() + "/"

print(path)

# Init script:
imf.script_init()

# Get list of images:
images_list = imf.get_image_list(dir=path)

# Create service directory:
imf.create_directory(tmp)

# Enhance the images(you can change defined coefficients):
images_list = list(map(lambda image: imf.enhance(image), images_list))

# Slice images(you can change defined number of splits):
images_list = list(map(lambda image: imf.slice_image(image=image), images_list))

# Flat the list of sliced images:
images_list = list(itertools.chain(*images_list))

# if image list not empty
if images_list:
    # Write images to service directory:
    images_list = list(map(lambda image: imf.wite_image(image=image, path=tmp), images_list))

    # Creating PDF:
    imf.create_pdf(sources_path=tmp, result_path=path)

    # Deleting service directory:
    imf.delete_directory(path=tmp)

    # Compress sources to archive:
    imf.compress_files(path=path)

    # Delete sources:
    imf.remove_sources(path=path)
else:
    print(imf.WARNING + "No file to make PDF!")
    # Deleting service directory:
    imf.delete_directory(path=tmp)
