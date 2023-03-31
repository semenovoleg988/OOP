class WindowDlg:
    def __init__(self, title, width, height) -> None:
        self.__title = title
        self.__width = self.__height = None
        self.width = width
        self.height = height

    @staticmethod
    def check_size(size):
        if isinstance(size, int) and 0 <= size <= 1000:
            return True
        return False

    def show(self):
        print(f"{self.__title}: {self.__width}, {self.__height}")

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, width):
        if self.check_size(width):
            self.__width = width
        self.show()

    @width.deleter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if self.check_size(height):
            self.__height = height
        self.show()

    @height.deleter
    def height(self, height):
        self.__height = height

