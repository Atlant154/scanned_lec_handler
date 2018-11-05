# Scanned lectures handler

![logo](doc/logo.png)

The implementation of the script allows for color correction, cropping and packing in PDF.

## Main features

1. **Color correction.**  
Color correction is made using the Pillow library. The following parameters are adjusted: color, brightness, contrast, sharpness.
The preset values give good results on scanned images.
2. **Image splitting.**  
To obtain a format of images suitable for viewing on mobile devices, vertical separation of the slide was used.
Due to the fact that a simple separation may violate content, an algorithm for smart cropping has been implemented.
The line with the most white pixels is determined and being used as a cropping line.  
At the moment, when splitting into more than two parts, the result may be incorrect.

## Requirements

1. [Python 3.*](https://www.python.org/downloads/): img2pdf, zipfile, shutil, math, os.
2. [Pillow](https://pillow.readthedocs.io/en/5.3.x/).

## How to run

1. Clone the repo: `git clone https://github.com/Atlant154/scanned_lec_handler.git`
2. Place images in `.png` format in a directory with `img_handler.py` script.
3. Comment out or change the lines in the `img_handler.py` if necessary.
4. Run the script by you interpreter.
