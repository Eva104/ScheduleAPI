from rest_framework import serializers
from .models import *


# Преподаватель
class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields = ['surname', 'name', 'patronymic', 'position', 'chair', 'work_time']


# Кафедра
class ChairSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chair
        fields = ['name', 'faculty']


# Рабочее время преподавателя
class Work_timeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Work_time
        fields = [  # 'monday','tuesday','wednesday','thursday','friday',
            'corps_index', 'corps_number']


# Факультет
class FacultySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Faculty
        fields = ['name']


# Направление
class DirectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Direction
        fields = ['code', 'name', 'chair', 'qualification']


# Группа
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields: ['name', 'amount', 'direction']


# Подгруппа
class SubgroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subgroup
        fields: ['amount', 'group_parent']


# Расписание экзамена
class Exam_scheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exam_schedule
        fields: ['name', 'date', 'groups']


# Расписание занятия
class Class_scheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Class_schedule
        fields: ['groups', 'teacher', 'room', 'discipline_name', 'week_day', 'periodicity', 'start_time', 'end_time']


# Аудитория
class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields: ['number', 'type_room', 'capacity', 'corps_index', 'corps_number']
