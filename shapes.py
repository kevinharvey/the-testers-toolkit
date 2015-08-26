import math

from twitter import tweet


class Rectangle(object):

    def __init__(self, width, height, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def broadcast(self):
        message = 'My rectangle is {} by {}'.format(self.width, self.height)
        tweet(message)


class Cylinder(object):

    def __init__(self, radius, height, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.radius = radius
        self.height = height
        
    def area_of_base(self):
        return math.pi * (self.radius ** 2)

    def volume(self):
        return self.area_of_base() * self.height
