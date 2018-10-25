import  img_handler_functions as imf

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

for image in image_list:
    imf.slice(image, 3, tmp, save=True)

# Delete service directory:
imf.delete_directory(tmp)