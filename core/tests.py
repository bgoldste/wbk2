"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from wbk2.tasks import getForecastData, getHeaderTitles, getAllData



class ModelTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """

        data = getForecastData(getAllData())
        print "adsad", data[0][0], data[0][1]
        self.assertEqual(type(data[0][0]), type(data[1][1]))

