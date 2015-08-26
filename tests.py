import unittest

from shapes import Rectangle


class RectangleTestCase(unittest.TestCase):

    def test_rectangle_area(self):
        """
        Test that we can calculate the area of a rectangle
        """
        rectangle = Rectangle(width=7, height=8)

        area = rectangle.area()

        self.assertEqual(area, 56)


if __name__ == '__main__':
    unittest.main()


# This test will be picked up by Nose, but not by running 
# this file as a script, or with Django
def test_rectangle_area_again():
    """
    Test that we can calculate the area of a rectangle
    """
    rectangle = Rectangle(width=8, height=8)

    area = rectangle.area()

    assert area == 64