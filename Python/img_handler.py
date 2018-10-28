from Python import img_handler_functions as imf

# Service directory:
tmp = "./TMP"

# Target directory:
path = './'

# Init script:
imf.script_init()

# Get list of images:
image_list = imf.get_image_list(dir=path)

# Create service directory:
imf.create_directory(tmp)

# Enhance images:
image_list = list(map(lambda x: imf.enchance(image=x), image_list))

if image_list:
    # Writing images in service directory:
    image_list = list(map(lambda x: imf.wite_image(image=x, number=image_list.index(x), path=tmp), image_list))
    # Creating PDF:
    imf.create_pdf(sources_path=tmp, result_path=path)
else:
    print(imf.WARNING + "No file to make PDF!")

# Deleting service directory:
imf.delete_directory(path=tmp)

# Compress sources to archive:
imf.compress_files(path=path)