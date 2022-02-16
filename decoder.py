# string.encode('utf-8')
# aa = "{:08b}".format(int(ss.hex(), 16)).zfill(32)
# bins = "{:08b}".format(int(ss.hex(), 16))
# bytes([int(x,2) for x in bins]).decode('utf-8')
from image_man import *
from text_man import save_file

null = '00000000'

def read_11_pixels(im: Image, pix, x: int, y: int) -> list:
    """
    Reads 11 pixels from the image and returns them as a list of strings.
    """
    bits = []
    for i in range(11):
        pixel = get_rgba_pixel(pix, x, y)
        bits.extend([pixel[i]%2 for i in range(3)])
        x += 1
        if x == im.size[0]:
            x = 0
            y += 1
    pixels = [bits[i:i+8] for i in range(0, len(bits), 8)][:-1]
    pixels = [''.join([str(c) for c in i]) for i in pixels]
    return pixels, x, y

def strip_bits(bits: list) -> list:
    """
    remove the null bits at the end of the file
    """
    return list(filter(lambda x: x != null, bits))

def extract_bits(im: Image, pix) -> list:
    """
    Extracts the bits from the image and returns them as a list of strings.
    """
    extracted_bits = []
    x, y, eof = 0, 0, False

    # iterating through pixels:
    while not eof:
        new_bits, x, y = read_11_pixels(im, pix, x, y)
        extracted_bits.extend(new_bits)
        if new_bits == [null]*4:
            eof = True
    return extracted_bits

def decode_bits(bits: list) -> str:
    return bytes([int(x,2) for x in bits]).decode('utf-8')

def init_decode(imagesrc):
    """
    Initializes the decoder and returns the decoded text.
    """
    # Reading the image
    im, pix = read_image(imagesrc)
    extracted_bits = extract_bits(im, pix)
    stripped_bits = strip_bits(extracted_bits)
    decoded_str = decode_bits(stripped_bits)

    save_file(imagesrc+'decoded.txt', decoded_str)