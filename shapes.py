class Rectangle(object):

    def __init__(self, width, height, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
