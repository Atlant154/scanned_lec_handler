# Scanned lectures handler

![logo](doc/logo.png)

Script for bash linux. It is placed in the directory with scans, it is launched, after which it will produce color correction, slice into slides(divide scan in half), convert it into `jp2`, pack it into PDF, optimally compress PDF, pack the used scans into the `zip` archive.

## Requirements

### Critical

1. [ImageMagick](https://www.imagemagick.org/script/index.php).
2. [img2pdf](https://github.com/josch/img2pdf).

### Non-critical

1. [ps2pdf](https://www.ghostscript.com/doc/current/Ps2pdf.htm).
2. zip

### How to install dependencies

You can install all dependencies using command: `sudo apt install ImageMagicl img2pdf ps2pdf zip`

## How to

Place the script in a directory with cropped and rotated scans, note that the file name should not contain spaces. Run the script, wait for the end. If you do not want to delete the uncompressed version of PDF or compress the photos - comment out the relevant lines in the script.
