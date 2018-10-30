import img_handler_functions as imf
import os

# Service directory:
tmp = "./TMP"

# Target directory:
path = os.getcwd() + "/"

print(path)

# Init script:
imf.script_init()

# Get list of images:
image_list = imf.get_image_list(dir=path)

# Create service directory:
imf.create_directory(tmp)

image_list = list(map(lambda image: imf.slice_image(image=imf.enhance(image=image), path=tmp), image_list))

# if image list not empty
if image_list:
    # Creating PDF:
    imf.create_pdf(sources_path=tmp, result_path=path)
else:
    print(imf.WARNING + "No file to make PDF!")

# Deleting service directory:
imf.delete_directory(path=tmp)

# Compress sources to archive:
imf.compress_files(path=path)

# Delete sources:
imf.remove_sources(path=path)
