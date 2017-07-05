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
    # check if the user has added courses previously
    if request.session.get('code_list'):
        # return the index with a list of the courses the user had put previously
        return render(request, 'api/index.html', {'code_list': request.session['code_list']})
    else:
        return render(request, 'api/index.html', {'code_list': None})
    
def clear_table(request):
    # clear the session holding the list of course codes the user had entered previously
    request.session['code_list'] = ''
    return JsonResponse({'status' : 'success', 'code' : 'The Table Has Been Cleared' })
    
def day_end_point(request):
    queryset = {}
    days = list(Day.objects.all())
    params = request.GET.getlist("code", None)

    # check if the code_list session exists
    if request.session.get('code_list'):
        if (params is not None):

            # loop through the course codes the user inputs
            for x in params:
                request.session['code_list'] += '-' + x

            # make the a unique list of the user's current course code list
            unique_code_list = set(request.session.get('code_list').split('-'))

            # get a list of class object that have the course codes entered
            class_objects = [class_obj for class_obj in Class.objects.filter(course__name__in=unique_code_list)]

            # if no class exist then the user input must be wrong and the session must be cleared
            if len(class_objects) == 0:
                request.session['code_list'] = ''

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
    else:
        request.session['code_list'] = ''
        if (params is not None):

            # loop through the course codes the user inputs
            for x in params:
                request.session['code_list'] += '-' + x

            # make the a unique list of the user's current course code list
            unique_code_list = set(request.session.get('code_list').split('-'))

            # get a list of class object that have the course codes entered
            class_objects = [class_obj for class_obj in Class.objects.filter(course__name__in=unique_code_list)]

            # if no class exist then the user input must be wrong and the session must be cleared
            if len(class_objects) == 0:
                request.session['code_list'] = ''

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