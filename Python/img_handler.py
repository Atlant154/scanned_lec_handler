from Python import img_handler_functions as imf
import multiprocessing as mulpro

# Service directory:
tmp = "./TMP"

# Target directory:
path = './'

# Init script:
imf.script_init()

# Get list of images:
image_list = imf.get_image_list(dir=path)

# Test output:
list(map(lambda x: print(x.filename), image_list))

# Create service directory:
imf.create_directory(tmp)

# Achtung!
pool = mulpro.Pool(processes=mulpro.cpu_count())

image_list = list(pool.map(imf.enhance, image_list))

pool.close()
# Achtung! end

# Sync stable:
# image_list = list(map(lambda x: imf.enhance(image=x), image_list))

# if image list not empty
if image_list:
    # Writing images in service directory:
    image_list = list(map(lambda x: imf.wite_image(image=x, path=tmp), image_list))
    # Creating PDF:
    imf.create_pdf(sources_path=tmp, result_path=path)
else:
    print(imf.WARNING + "No file to make PDF!")

# Deleting service directory:
imf.delete_directory(path=tmp)

# Compress sources to archive:
# imf.compress_files(path=path)