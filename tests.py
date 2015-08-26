import unittest
from unittest import TestCase, mock

from shapes import Rectangle, Cylinder


class RectangleTestCase(TestCase):

    def test_rectangle_area(self):
        """
        Test that we can calculate the area of a rectangle
        """
        rectangle = Rectangle(width=7, height=8)

        area = rectangle.area()

        self.assertEqual(area, 56)


class CylinderTestCase(TestCase):

    def test_cylinder_area_of_base(self):
        """
        Test that we can calculate the area of a cylinder's base
        """
        cylinder = Cylinder(radius=2, height=7)

        area = cylinder.area_of_base()

        self.assertAlmostEqual(area, 12.6, places=1)

    @mock.patch('shapes.Cylinder.area_of_base')
    def test_cylinder_volume(self, mock_area):
        """
        Test that we can calculate the volume of a cylinder
        """
        mock_area.return_value = 5

        cylinder = Cylinder(radius=2, height=7)

        self.assertEqual(cylinder.volume(), 35)


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
