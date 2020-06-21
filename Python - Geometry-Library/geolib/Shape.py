class Shape:
    """
    The superclass Shape
    """

    def __init__(self, name='Shape'):
        self.name = name

    def __str__(self):
        return 'Shape : {}'.format(self.name)

    def __repr__(self):
        return self.__str__()
