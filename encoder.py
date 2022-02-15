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
###################################################################################################

from image_man import *
from text_man import *

def init_encode(code_bits: str, imagesrc: str):
    im, pix = read_image(imagesrc)
    if image_pixel_count(im) < len(code_bits):
        print("This text is too large for this picture (size mismatch error)")
        return 2
    pass