#!/usr/bin/python3
"""Define class square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class square  that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """init"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str"""
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.height)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, size):
        """size setter"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Update class Square by adding public method assigns attributes"""
        for i in range(len(args)):
            if i == 0:
                self.id = args[0]
            if i == 1:
                self.width = args[1]
                self.height = args[1]
            if i == 2:
                self.x = args[2]
            if i == 3:
                self.y = args[3]
        else:
            for key, val in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, val)
    def to_dictionary(self):
        """dictionary representation of a square"""
        dic = {}
        dic["id"] = self.id
        dic["x"] = self.x
        dic["size"] = self.width
        dic["y"] = self.y
        return dic
