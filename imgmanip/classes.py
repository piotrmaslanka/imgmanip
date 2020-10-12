import typing as tp
from PIL import Image as PILImage


class Image:
    def __init__(self, path: str):
        self.path = path
        self.image = PILImage.open(path)
        self.width, self.height = self.image.size

    def save(self):
        self.image.save(self.path)

    def __iter__(self):
        return ImageIterator(self)

    def getpixel(self, x, y):
        return self.image.getpixel((x, y))

    def setpixel(self, x, y, value):
        self.image.putpixel((x, y), value)


class PixelValue:
    __slots__ = ('image', 'x', 'y')

    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y

    @property
    def r(self) -> float:
        return self.image.getpixel(self.x, self.y)[0]

    @property
    def g(self) -> float:
        return self.image.getpixel(self.x, self.y)[1]

    @property
    def b(self) -> float:
        return self.image.getpixel(self.x, self.y)[2]

    @property
    def a(self) -> float:
        return self.image.getpixel(self.x, self.y)[3]

    @r.setter
    def r(self, value: float):
        px = self.image.getpixel(self.x, self.y)
        px = (value, *px[1:])
        self.image.setpixel(self.x, self.y, px)

    @g.setter
    def g(self, value: float):
        px = self.image.getpixel(self.x, self.y)
        px = (px[0], value, *px[2:])
        self.image.setpixel(self.x, self.y, px)

    @r.setter
    def b(self, value: float):
        px = self.image.getpixel(self.x, self.y)
        px = (px[0], px[1], value, *px[3:])
        self.image.setpixel(self.x, self.y, px)

    @a.setter
    def a(self, value: float):
        px = self.image.getpixel(self.x, self.y)
        px = (px[0], px[1], px[2], value)
        self.image.setpixel(self.x, self.y, px)

    @property
    def value(self) -> tp.Tuple[float, ...]:
        return self.image.getpixel(self.x, self.y)

    @value.setter
    def value(self, value: tp.Tuple[float, ...]):
        self.image.setpixel(self.x, self.y, value)


class ImageIterator:
    def __init__(self, image: Image):
        self.image = image
        self.x, self.y = 0, 0

    @property
    def coords(self) -> tp.Tuple[int, int]:
        return self.x, self.y

    def next_pixel(self):
        max_width, max_height = self.image.width, self.image.height
        if self.x == max_width - 1  and self.y == max_height - 1:
            raise StopIteration()

        if self.x == self.image.width - 1:
            self.y += 1
            self.x = 0
        else:
            self.x += 1

    def __next__(self):
        self.next_pixel()
        return PixelValue(self.image, self.x, self.y)

    def __iter__(self):
        return self

