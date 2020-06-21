from math import pi

from geolib.Shape import Shape


class Circle(Shape):
    """
    The Circle class
    """

    def __init__(self, radius=1.0):
        self.name = 'Circle'
        if radius < 0:
            raise ValueError('Radius should not be negative')
        self._radius = radius

    def set_radius(self, radius):
        if radius < 0:
            raise ValueError('Radius should not be negative')
        self._radius = radius

    def get_radius(self):
        return self._radius

    def get_area(self):
        """Return the area of the Circle"""
        return pi * (self.get_radius() ** 2)

    def project(self, length=1.0):
        """Return projected circle as Cylinder object"""
        return Cylinder(self.get_radius(), length)

    def __str__(self):
        return 'Shape : {}, with radius {}'.format(self.name, self._radius)

    def __repr__(self):
        return self.__str__()


class Cylinder(Circle):
    """
    The Cylinder class
    """

    def __init__(self, radius=1.0, length=1.0):
        self.name = 'Cylinder'
        if radius < 0 or length < 0:
            raise ValueError('Radius or Length should not be negative')
        super().__init__(radius)
        self._length = length

    def set_length(self, length):
        if length < 0:
            raise ValueError('Length should not be negative')
        self._length = length

    def get_length(self):
        return self._length

    def get_area(self):
        """Return the surface area of the Cylinder"""
        return (2 * pi * self.get_radius() * self.get_length()) + (2 * super().get_area())

    def get_volume(self):
        """Return the volume of the Cylinder"""
        return super().get_area() * self.get_length()

    def flatten(self):
        """Return flattened Cylinder as Circle object"""
        return Circle(self.get_radius())

    def __str__(self):
        return 'Shape : {}, with radius {} and length {}'.format(self.name, self._radius, self._length)

    def __repr__(self):
        return self.__str__()
