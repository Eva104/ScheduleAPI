from django.urls import re_path
from rest_framework import viewsets

from .models import (
    Teacher,
    Chair,
    Work_time,
    Faculty,
    Direction,
    Group,
    Subgroup,
    Exam_schedule,
    Class_schedule,
    Room
)

from .serializers import (
    TeacherSerializer,
    ChairSerializer,
    Work_timeSerializer,
    FacultySerializer,
    DirectionSerializer,
    GroupSerializer,
    SubgroupSerializer,
    Exam_scheduleSerializer,
    Class_scheduleSerializer,
    RoomSerializer
)


def get(self, request, pk: int):
    return super().get(request, pk=pk)


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def get(self, request, pk: int):
        return super().retrieve(request, pk=pk)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class ChairViewSet(viewsets.ModelViewSet):
    queryset = Chair.objects.all()
    serializer_class = ChairSerializer


class Work_timeViewSet(viewsets.ModelViewSet):
    queryset = Work_time.objects.all()
    serializer_class = Work_timeSerializer


class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class DirectionViewSet(viewsets.ModelViewSet):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class SubgroupViewSet(viewsets.ModelViewSet):
    queryset = Subgroup.objects.all()
    serializer_class = SubgroupSerializer


class Exam_scheduleViewSet(viewsets.ModelViewSet):
    queryset = Exam_schedule.objects.all()
    serializer_class = Exam_scheduleSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class Class_scheduleViewSet(viewsets.ModelViewSet):
    queryset = Class_schedule.objects.all()
    serializer_class = Class_scheduleSerializer
