from rest_framework import serializers
from .models import Course, Day, Class
 
class CourseSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Course
        fields = ("name", "day",)
 
class ClassSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source='course.name')
    day = serializers.ReadOnlyField(source='day.name')
 
    class Meta:
        model = Class
        fields = ("course", "day", "time", "venue",)
 
class DaySerializer(serializers.HyperlinkedModelSerializer):

    classes = ClassSerializer(many=True)
    # day = DaySerializer()

    class Meta:
        model = Day
        fields = ("id", "name", "classes",)