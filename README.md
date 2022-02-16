
# UTF-8 image steganopgrahy

A very simple (and un-optimized) steganopgrahy app used for hiding a secret message(txt)
in an image file



## How it works

This code seperates each character into 4 bytes (since a UTF-8 character will take 4 at most)
and converts them to binary.

It then gives each 11 consequetive pixels in the picture a character, by setting RGB values in RGB and RGBA modes or CMY in CMYK pictures even and odd, for each 1 or 0 in the bits

#### Example:
if we had **01101001** as the secret message, and our pixels had the values:
>(128, 127, 222), (201, 198, 23), (100, 108, 202)
the pixels would change to:
>(128, 127, 221), (200, 197, 24), (100, 109, 202)

So that when we want to read it, we can just read the oddity of pixel color values and put them together, untill we reach 4 consequetive NULL bytes (00000000)


****
## Using the program
First clone the repository using `git clone https://github.com/Taha-Alikhani/utf8_image_steganography`

and inside the directory run:
`python3 main.py -f <Text file address> -i <Image file address>`
or 
`python3 main.py -c <1 line of text> -i <Image file address>`

The picture file with the code hidden inside it will be saved as `<original name>_encoded`
and you can retrieve the text inside it via 
`python3 main.py -d <Encoded Image file address>`
