from django.test import TestCase

from .models import Person


class PersonTestCase(TestCase):
	
	def test_person_full_name(self):
		"""
		Test that we can get a person's full name
		"""
		person = Person(first_name='Steve', last_name='Rogers')
		
		self.assertEqual(person.full_name, 'Steve Rogers')
