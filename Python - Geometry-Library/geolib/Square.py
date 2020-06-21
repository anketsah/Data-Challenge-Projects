from geolib.Shape import Shape


class _Rectangle(Shape):
    """
    The Rectangle class
    """

    def __init__(self, length=1.0, width=1.0):
        self.name = 'Rectangle'
        self._length = length
        self._width = width

    def _set_length(self, length):
        if length < 0:
            raise ValueError('Length should not be negative')
        self._length = length

    def _get_length(self):
        return self._length

    def _set_width(self, width):
        if width < 0:
            raise ValueError('Width should not be negative')
        self._width = width

    def _get_width(self):
        return self._width

    def get_area(self):
        """Return the area of the Rectangle"""
        return self._get_length() * self._get_width()

    def __str__(self):
        return 'Shape : {}, with length {} and width {}'.format(self.name, self._length, self._width)

    def __repr__(self):
        return self.__str__()


class Square(_Rectangle):
    """
    The Square class
    """

    def __init__(self, length=1.0):
        self.name = 'Square'
        if length < 0:
            raise ValueError('Length should not be negative')
        super().__init__(length, length)

    def set_length(self, length):
        if length < 0:
            raise ValueError('Length should not be negative')
        super()._set_length(length)
        super()._set_width(length)

    def get_length(self):
        return super()._get_length()

    def project(self):
        """Return projected Square as Cube object"""
        return Cube(self.get_length())

    def __str__(self):
        return 'Shape : {}, with length {}'.format(self.name, self._length)

    def __repr__(self):
        return self.__str__()


class Cube(Square):
    """
    The Cube class
    """

    def __init__(self, length=1.0):
        self.name = 'Cube'
        super().__init__(length)

    def __str__(self):
        return 'Shape : {}, with length {}'.format(self.name, self._length)

    def get_area(self):
        """Return the surface area of the Cube"""
        return 6 * (self.get_length() ** 2)

    def get_volume(self):
        """Return the volume of the Cube"""
        return self.get_length() ** 3

    def flatten(self):
        """Return flattened Cube as Square object"""
        return Square(self.get_length())

    def __repr__(self):
        return self.__str__()
