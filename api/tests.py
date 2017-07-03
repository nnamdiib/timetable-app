from __future__ import unicode_literals
from rest_framework.test import APIClient
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