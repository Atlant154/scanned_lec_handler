from Python import img_handler_functions as imf

# Service directory:
tmp = "./TMP"

# Target directory:
path = './'

print(imf.INFO + "Supported formats: " + str(imf.image_ext));

print(imf.SUCCESS + "Script is running!")

print(imf.INFO + "Start scanning the directory!")

image_list = imf.get_image_list(path)

# Create service directory:
imf.create_directory(tmp)

image_list = list(map(lambda x: imf.enchance(x, 30), image_list))

image_list = list(map(lambda x: imf.wite_image(x, image_list.index(x), tmp), image_list))

imf.create_pdf(tmp, path)

imf.delete_directory(tmp)

# Delete service directory:
# imf.delete_directory(tmp)
