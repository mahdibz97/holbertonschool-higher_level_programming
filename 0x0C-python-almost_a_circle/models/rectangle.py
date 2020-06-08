#!/usr/bin/python3
"""Define class rectangele"""


from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None): 
        """init"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError ("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """height"""
        return(self.__height)

    @height.setter
    def height(self, height):
        """height setter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """x"""
        return(self.__x)

    @x.setter
    def x(self, x):
        """x setter"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y"""
        return(self.__y)

    @y.setter
    def y(self, y):
        """y setter"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """return the area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """print the rectangle instance with the character #"""
        for j in range(self.y):
            print("")
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """str"""
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__width, self.__height, self.__x, self.__y)
            
    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        j = 0
        if len(args):
            for i in args:
                j += 1
                if j == 1:
                    self.id = i
                if j == 2:
                    self.width = i
                if j == 3:
                    self.height = i
                if j == 4:
                    self.x = i
                if j == 5:
                    self.y = i
        else:
            for c, d in kwargs.items():
                setattr(self, c, d)