###################################################################################################
# The maximum number of bytes per character for UTF-8 is 4 which is 32 bits.                      #
# Since not every format supports transparency we are saving on RGB bits instead of RGBA.         #
# Thus we need 11 pixels per character. (11*3 = 33 > 32)                                          #
###################################################################################################
# Encoding algorithm:                                                                             #
# For every bit on the character, we change the RGB value of the pixel, using this policy:        #
# For each 1: Set to Odd, for each 0: Set to Even                                                 #
# We ++ in encoding if RGB value is bigger than or equal to 128                                   #
# We -- in encoding if RGB value is smaller than 128                                              #
# The above action is not reversible, but who cares? we are not gonna need the original image.    #
###################################################################################################

from image_man import *

def hide_3_bits(pix, x: int, y: int, bits: list):
    pixel = get_rgba_pixel(pix, x, y)
    sign = [-1+2*(int(bits[j]) <= 128) for j in range(3)]
    for i in range(3):
        if bits[i]%2 != pixel[i]%2:
            pixel[i] += sign[i]

def init_encode(code_bits: str, imagesrc: str):
    # Read the image
    im, pix = read_image(imagesrc)

    # if the image is too small, we cannot hide the text
    if image_pixel_count(im) < len(code_bits):
        print("The text is too large for this picture {%d/%d} (size mismatch error)" % (len(code_bits), image_pixel_count(im)))
        return 2
    
    # write the code to the image
    x, y = 0, 0
    for i in range(0, len(code_bits), 32):
        # add another byte to the end of the bits to make it's length divisible by 3
        bits_33 = code_bits[i:i+32] + str(get_33rd_byte(im, pix, x, y)%2)

        for j in range(11):
            # hide the 3 bits in each pixel
            hide_3_bits(pix, x, y, bits_33[j*3:j*3+3])
    
    write_image(im, imagesrc.replace('.', '_encoded.'))