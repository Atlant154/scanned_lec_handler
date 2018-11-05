# Scanned lectures handler

![logo](doc/logo.png)

The implementation of the script allows for color correction, cropping and packing in PDF.

## Main functions

1. Color correction.
Color correction is made using the library Pillow. The following parameters are adjusted: color, brightness, contrast, sharpness. The preset values give good results on scanned images.
2. Image splitting.
To get the slide suitable for viewing from mobile devices used to split the image vertically. Since the geometric division can divide the text on a line, a smart algorithm has been implemented: a white line is automatically found between the text and the division occurs according to it.
At the moment, when splitting into more than two parts, the result may be incorrect.

## Requirements

1. [Python 3.*](https://www.python.org/downloads/): img2pdf, zipfile, shutil, math, os.
2. [Pillow](https://pillow.readthedocs.io/en/5.3.x/).

## How to run

1. Clone the repo: `gir clone https://github.com/Atlant154/scanned_lec_handler.git`
2. Place photos in `.png` format in a directory with `img_handler.py` script.
3. Comment out or change the lines in the `img_handler.py` if necessary.
4. Run the script by you interpreter.
