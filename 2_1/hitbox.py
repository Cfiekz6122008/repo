class Hitbox:
    def __init__(self, x, y, width, heigth):

        self.__x = x
        self.__y = y
        self.__set_width(width)
        self.__set_height(heigth)



    def __get_width(self):
        return self.__width

    def __set_width(self, width):
        if width < 0 :
            width = 0
        self.__width = width

    def __get_height(self):
        return self.__height

    def __set_height(self, height):
        if height < 0 :
            height = 0
        self.__height = height

    def __get_x(self):
        return self.__x

    def __set_x(self, x):
        self.__x = x

    def __get_y(self):
        return self.__y

    def __set_y(self, y):
        self.__y = y

    def __str__(self):
        return f"({self.__x=}, {self.__y=}, {self.__width=}, {self.__height=})"

 #   x = property(__get_x, __set_x)
  #  y = property(__get_y, __set_y)
   # width = property(__get_width, __set_width)
    #heigth = property(__get_height, __set_height)


