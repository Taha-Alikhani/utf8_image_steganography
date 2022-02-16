from PIL import Image

class RGBA:
    """
    RGBA class is used to represent a pixel in an image using RGBA values.
    """
    def __init__(self, r, g, b, a):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def __repr__(self):
        return '({}, {}, {}, {})'.format(self.r, self.g, self.b, self.a)
    
    def __eq__(self, other):
        return self.r == other.r and self.g == other.g and self.b == other.b and self.a == other.a

    def __iter__(self):
        return iter([self.r, self.g, self.b, self.a])
    
    def __getitem__(self, index):
        return [self.r, self.g, self.b, self.a][index]

    def __setitem__(self, index, value):
        if index == 0:
            self.r = value
        elif index == 1:
            self.g = value
        elif index == 2:
            self.b = value
        elif index == 3:
            self.a = value
        else:
            raise IndexError('Index out of range')

def read_image(filename):
    """
    Reads an image from a file and returns it as a PIL Image object and pixels.
    """
    im = Image.open(filename)
    pix = im.load()
    return im, pix

def image_pixel_count(im) -> int:
    """
    Returns the number of pixels in the image.
    """
    return im.size[0] * im.size[1]

def write_image(im: Image.Image, filename: str):
    """
    Writes an image to a file.
    """
    im.save(filename)

def get_pixel(pix, x, y) -> tuple:
    """
    Returns the pixel at the given coordinates.
    """
    return pix[x, y]

def get_rgba_pixel(pix, x, y) -> RGBA:
    """
    Returns the pixel at the given coordinates as an RGBA object.
    """
    return RGBA(*pix[x, y])

def get_33rd_byte(im, pix, x, y) -> int:
    """
    Returns the 33rd byte of the pixel after the given coordinates.
    """
    width = im.size[0]
    return (pix[((x +11)%width)-1, y + ((x+11)//width)])[2]

def set_pixel(pix, x, y, pixel: tuple):
    """
    Sets the pixel at the given coordinates to the given pixel tuple.
    """
    pix[x, y] = pixel

def set_rgba_pixel(pix, x, y, pixel: RGBA):
    """
    Sets the pixel at the given coordinates to the given RGBA object.
    """
    pix[x, y] = (pixel.r, pixel.g, pixel.b, pixel.a)
