import unittest
from unittest import TestCase, mock

import vcr

from shapes import Rectangle, Cylinder
from twitter import list_twitter_repos


class RectangleTestCase(TestCase):

    def setUp(self):
        self.rectangle = Rectangle(width=7, height=8)

    def test_rectangle_area(self):
        """
        Test that we can calculate the area of a rectangle
        """
        area = self.rectangle.area()

        self.assertEqual(area, 56)

    @mock.patch('shapes.tweet')
    def test_rectangle_broadcast(self, mock_tweet):
        """
        Tests that we call tweet with a formatted message
        """
        self.rectangle.broadcast()

        mock_tweet.assert_called_with('My rectangle is 7 by 8')


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
		

class TwitterTestCase(TestCase):
	
	def test_list_twitter_repos(self):
		"""
		Test that we can get a list of Twitter's repos
		"""
		with vcr.use_cassette('vcr/list_twitter_repos.yaml'):
			repos = list_twitter_repos()
		
		self.assertEqual(repos[0], 'kestrel')

	def test_list_twitter_repos_error(self):
		"""
		Test that we fail gracefully if the GitHub API is down
		"""
		with vcr.use_cassette('vcr/list_twitter_repos_error.yaml'):
			repos = list_twitter_repos()
		
		self.assertEqual(repos, 'The GitHub API is currently unavailable')
		

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
