class Rectangle:
    """A representation of a rectangle shape"""
    def __init__(self, width: int, height: int):
        """Initialize the width and height of the object"""
        self.width = width
        self.height = height

    def set_width(self, width: int):
        """Set the width of the object"""
        self.width = width

    def set_height(self, height: int):
        """Set the the height of the object"""
        self.height = height

    def get_area(self):
        """Returns the area of the object"""
        return self.width * self.height

    def get_perimeter(self):
        """Returns the perimeter of the object"""
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        """Returns the diagonal of the object"""
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        """Returns a string representation of the object, unless the height or width is > 50"""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return f"{'*' * self.width}\n" * self.height

    def get_amount_inside(self, shape):
        """Returns how much of a specific object can fit into this object

        :type shape: Rectangle or Square"""
        return (self.width // shape.width) * (self.height // shape.height)

    def __str__(self):
        """Returns the width and height of the Rectangle when print() is called on it"""
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    """A representation of a square, inherited from the Rectangle class"""
    def __init__(self, side: int):
        """Initializes the length of the side of the square"""
        self.side = side
        self.height = side
        self.width = side

    def set_side(self, side):
        """Sets the length of the side of the square"""
        self.side = side
        self.height = side
        self.width = side

    def set_width(self, width):
        """Sets the width of the square to be the same as its side"""
        self.side = width
        self.height = width
        self.width = width

    def set_height(self, height):
        """Sets the height of the square to be the same its side"""
        self.side = height
        self.height = height
        self.width = height

    def __str__(self):
        """Returns the side of the Square when print() is called on it"""
        return f"Square(side={self.side})"
