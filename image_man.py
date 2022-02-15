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

def read_image(filename):
    """
    Reads an image from a file and returns it as a PIL Image object and pixels.
    """
    im = Image.open(filename)
    pix = im.load()
    return im, pix

def image_pixel_count(im):
    """
    Returns the number of pixels in the image.
    """
    return im.size[0] * im.size[1]

def write_image(im: Image.Image, filename: str):
    """
    Writes an image to a file.
    """
    im.save(filename)

def get_pixel(pix, x, y):
    """
    Returns the pixel at the given coordinates.
    """
    return pix[x, y]

def get_rgba_pixel(pix, x, y):
    """
    Returns the pixel at the given coordinates as an RGBA object.
    """
    return RGBA(*pix[x, y])

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
