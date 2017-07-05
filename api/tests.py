from __future__ import unicode_literals
from rest_framework.test import APIClient, RequestsClient
from rest_framework import status
from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import Day, Course, Class

# Create your tests here.
class ModelTestCase(TestCase):
  """
  This class defines the test suite for the Day, Course, Class models
  """

  def setUp(self):
    """Define the test variables"""

    self.day_name = "Monday"
    self.day = Day(name=self.day_name)

    self.course_name = "mat111"
    self.course = Course(name=self.course_name)

    self.time = "08am-10am"
    self.venue = "LT1"    

  def test_model_can_create_a_day(self):
    """Test if the Day model can create a Day object"""
    old_count = Day.objects.count()
    self.day.save()
    new_count = Day.objects.count()
    self.assertNotEqual(old_count, new_count)

  def test_model_can_create_a_course(self):
    """Test if the Course model can create a Course object"""
    old_count = Course.objects.count()
    self.course.save()
    new_count = Course.objects.count()
    self.assertNotEqual(old_count, new_count)

  def test_model_can_create_a_class(self):
    """Test if the Class model can create a Class object"""
    old_count = Class.objects.count()
    self.day.save()
    self.course.save()

    self.the_class = Class(course=self.course, day=self.day, time=self.time, venue=self.venue)
    self.the_class.save()

    new_count = Class.objects.count()
    self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
  """ Test suite for the API views """

  def setUp(self):
    """ define the test client and other variables """
    self.client = APIClient()

    # Since user model instance is not serializable, use its ID/PK
    self.course = Course(name="mat111")
    self.course.save()

  # def test_api_can_create_bucketlist(self):
  #   """ test if the api can really create a bucket list """
  #   self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

  def test_api_can_get_a_course(self):
    course = Course.objects.get(id=1)
    response = self.client.get(
                              '/dayend/',
                              kwargs={'code': 'mat111'},
                              format="json"
                              )

    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertContains(response, course)


