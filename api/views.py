from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .serializers import ClassSerializer, DaySerializer
from rest_framework import generics
from .models import Class, Course, Day

import json


class ClassListCreate(generics.ListCreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class ClassList(generics.ListAPIView):
    serializer_class = ClassSerializer

    def get_queryset(self):
        queryset = []
        
        params = self.request.query_params.get('codes', None)
        print("The params i received", params)
        
        if params is not None:
            params = params.split(',')
        
            for token in params:
                queryset.extend(Class.objects.filter(course__name=str(token)))

        return queryset

class DayListCreate(generics.ListCreateAPIView):
    
    queryset = Day.objects.all()
    serializer_class = DaySerializer

class DayList(generics.ListAPIView):
    
    queryset = Day.objects.all()
    serializer_class = DaySerializer

    def get_queryset(self):
        queryset = []

        days = list(Day.objects.all())

        params = self.request.query_params.get('codes', None)

        if params is not None:
            params = params.split('&')

        class_objects = [class_obj for class_obj in Class.objects.filter(course__name__in=params)]

        for day in days:
            classes_for_day = []
            for class_obj in class_objects:
                if (class_obj.day == day):
                    course_dict = {
                                    'course': class_obj.course,
                                    'time': class_obj.time,
                                    'venue': class_obj.venue
                                }
                    classes_for_day.append(course_dict)
            day_dict = {day.name : classes_for_day}
            queryset.append(day_dict)


        # queryset.extend(Day.objects.filter(courses__name__in=[params]))
        # queryset.extend(Day.objects.filter(classes__course__name__in=params))

        return queryset

def index(request):
    return render(request, 'api/index.html', {})

    
def day_end_point(request):
    queryset = {}
    days = list(Day.objects.all())
    params = request.GET.get("codes", None)

    if (params is not None):
        params = params.split(',')
        class_objects = [class_obj for class_obj in Class.objects.filter(course__name__in=params)]

        for day in days:
            classes_for_day = []
            for class_obj in class_objects:
                if (class_obj.day == day):
                    course_dict = {
                                    'course': class_obj.course.__str__().upper(),
                                    'time': class_obj.time,
                                    'venue': class_obj.venue,
                                    'day': class_obj.day.__str__()
                                  }
                    classes_for_day.append(course_dict)

            queryset[day.__str__()] = classes_for_day
    return JsonResponse(queryset)