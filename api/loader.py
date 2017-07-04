from .clamparser import magic
from .models import Course, Day, Class
import sys, os

PARSER_FILE_DIR = 'parserfiles'

def load_data(filelist):
  clear_db()
  days = list(Day.objects.all())
  del days[2] # remove this line when we get the Wednesday schedule.
  for i in range(len(filelist)):
    base_dir = os.path.join(os.getcwd(), PARSER_FILE_DIR)
    filepath = os.path.join(base_dir, filelist[i])
    courses = magic(filepath, days[i])
    existing_courses = [course.name for course in Course.objects.all()]

    for course_code in courses:
      if course_code in existing_courses:
        obj = Course.objects.filter(name=course_code)[0]
      else:
        obj = Course(name=course_code)
        obj.save()

      the_time = courses[course_code]['time']
      the_venue = courses[course_code]['venue']
      the_class = Class(course=obj, day=days[i], time=the_time, venue=the_venue)
      the_class.save()
      print("I just created %s for %s" %(course_code, days[i].name))

def load_specific_day(day, filelist):
    for i in range(len(filelist)):
      base_dir = os.path.join(os.getcwd(), PARSER_FILE_DIR)
      filepath = os.path.join(base_dir, filelist[i])
      courses = magic(filepath, day)
      existing_courses = [course.name for course in Course.objects.all()]

      for course_code in courses:
        if course_code in existing_courses:
          obj = Course.objects.filter(name=course_code)[0]
        else:
          obj = Course(name=course_code)
          obj.save()

        the_time = courses[course_code]['time']
        the_venue = courses[course_code]['venue']
        the_class = Class(course=obj, day=day, time=the_time, venue=the_venue)
        the_class.save()
        print("I just created %s for %s" %(course_code, day.name))

def clear_db():
  all_courses = Course.objects.all()
  all_courses.delete()
  print("**************")
  print("I have deleted all the 'Course' objects.")
  print("**************")
  print("\n\n")
  
  all_class = Class.objects.all()
  all_class.delete()
  print("**************")
  print(" I Deleted all 'Class' objects.")
  print("**************")
  print("\n\n")

print(os.path.join(os.getcwd(), PARSER_FILE_DIR))

