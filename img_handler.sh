#!/bin/bash

# Requirements: img2pdf ImageMagick ps2pdf zip

# Text highlighting colors:
ERR="$(tput setaf 1)"
SUC="$(tput setaf 2)"
WARN="$(tput setaf 3)"
INFO="$(tput setaf 4)"
NC="$(tput sgr0)"

# Create a service directory:
mkdir temp

echo "$INFO[info] Start color correction!$NC"

# Make color correction:
for file in $(ls *.png *.jpg *.bmp *.jpeg *.jp2); do
	{
		convert -auto-level -enhance -normalize -contrast $file ./temp/"${file%.*}.png"
	} || {
		echo "$ERR[Error] Color correction error!$NC"
		rm -R ./temp
		exit 1
	}
done

echo "$INFO[info] Color correction done! $NC"

cd temp

# Split image by two:
for image in *.png; do
	{
		convert -crop 100%x50% +repage $image "cropped_${image%.png}_%d.png" && rm ./$image
	} || {
		echo "$ERR[Error] Cropping error!$NC"
		cd .. 
		rm -R ./temp
		exit 1
	}
done

echo "$INFO[info] Images cropped!$NC"

for image in *.png; do
	{
		convert  $image -transparent white -quality 0 "${image%.png}.jp2" && rm ./$image
	} || {
		echo "$ERR[Error] Conversion error!$NC"
		cd ..
	       	rm -R ./temp
		exit 1
	}
done

echo "$INFO[info] Images converted!$NC"
{
	img2pdf -o ../result.pdf *.jp2 && echo "$WARN[Success] Uncompressed PDF created!$NC"
} || {
	echo "$ERR[Error] Creating uncompressed PDF error!$NC"
	cd ..
	rm -R ./temp
	rm result.pdf
	exit 1
}

cd ..

rm -R ./temp && echo "$WARN[Warning] Temporary files deleted!$NC"
{
	ps2pdf result.pdf compressed.pdf && echo "$SUC[Success] Compressed PDF created!$NC"
} || {
	echo "$ERR[Error] Creating compressed PDF error!$NC"
	rm ./compressed.pdf
	rm ./result.pdf
	exit 1
}

# Comment this if you don't need delete uncompressed PDF:
rm ./result.pdf && echo "$INFO[info] Uncompressed PDF deleted!$NC"

zip images.zip *.png && rm ./*.png && echo "$SUC[info] All images compressed!$NC"
