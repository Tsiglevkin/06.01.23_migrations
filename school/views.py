from django.http import HttpResponse
from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    """Функция возвращает рендер со списком студентов, упорядоченных по группе"""
    template = 'school/students_list.html'
    ordering = 'group'  # название столбца таблицы
    persons = Student.objects.order_by(ordering).prefetch_related('teachers')
    context = {
        'object_list': persons
    }

    return render(request, template, context)


def add_teachers(request):
    """Функция принимает request и добавляет каждому ученику всех доступных учителей"""
    students = Student.objects.all()
    teachers = Teacher.objects.all()

    for student in students:  # добавляем каждого учителя к каждому студенту.
        for teacher in teachers:
            student.teachers.add(teacher)

    return HttpResponse('Каждому ученику добавлены все учителя.')





