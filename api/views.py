from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .serializers import ClassSerializer, DaySerializer
from .models import Class, Course, Day

import json

def index(request):
    return render(request, 'api/index.html', {})


def class_end_point(request):
    queryset = []
    params = request.GET.getlist("code", None)
    if (params is not None):
        if(params[0] == 'all'):
            for class_obj in Class.objects.all():
                course_dict = {
                                'course': class_obj.course.__str__().upper(),
                                'time': class_obj.time,
                                'venue': class_obj.venue,
                                'day': class_obj.day.__str__()
                              }
                queryset.append(course_dict)
        else:     
            class_objects = [class_obj for class_obj in Class.objects.filter(course__name__in=params)]
            for class_obj in class_objects:
                course_dict = {
                                'course': class_obj.course.__str__().upper(),
                                'time': class_obj.time,
                                'venue': class_obj.venue,
                                'day': class_obj.day.__str__()
                              }
                queryset.append(course_dict)
    return JsonResponse(queryset, safe=False)

    
def day_end_point(request):
    queryset = {}
    days = list(Day.objects.all())
    params = request.GET.getlist("code", None)
    if (params is not None):
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