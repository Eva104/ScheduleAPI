from django.db import models


# * My models:

# Преподаватель
class Teacher(models.Model):
    surname = models.CharField(max_length=31)
    name = models.CharField(max_length=31)
    patronymic = models.CharField(max_length=31)
    position = models.CharField(max_length=31)
    chair = models.ForeignKey('Chair', null=True, on_delete=models.SET_NULL)
    work_time = models.OneToOneField('Work_time', null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

    def __str__(self):
        return f'{self.name} {self.surname}'


# Кафедра
class Chair(models.Model):
    name = models.CharField(max_length=31)
    faculty = models.ForeignKey('Faculty', null=True, on_delete=models.SET_NULL)


# Рабочее время преподавателя
class Work_time(models.Model):
    # monday =
    # tuesday =
    # wednesday =
    # thursday =
    # friday =
    corps_index = models.CharField(max_length=7)
    corps_number = models.PositiveIntegerField()


# Факультете
class Faculty(models.Model):
    name = models.CharField(max_length=31)


# Направление
class Direction(models.Model):
    code = models.CharField(max_length=15, primary_key=True)  # id
    name = models.CharField(max_length=31)
    chair = models.ForeignKey('Chair', null=True, on_delete=models.SET_NULL)
    qualification = models.CharField(max_length=63)


# Группа
class Group(models.Model):
    name = models.CharField(max_length=31)
    amount = models.PositiveIntegerField()
    direction = models.ForeignKey('Direction', null=True, on_delete=models.SET_NULL)


# Подгруппа
class Subgroup(models.Model):
    amount = models.PositiveIntegerField()
    group_parent = models.OneToOneField('Group', null=True, on_delete=models.SET_NULL)


# Расписание экзамена
class Exam_schedule(models.Model):
    name = models.CharField(max_length=63)
    date = models.DateField()
    groups = models.ForeignKey('Group', null=True, on_delete=models.SET_NULL)


# Расписание занятия
class Class_schedule(models.Model):
    groups = models.ForeignKey('Group', null=True, on_delete=models.SET_NULL)
    teacher = models.ForeignKey('Teacher', null=True, on_delete=models.SET_NULL)
    room = models.OneToOneField('Room', null=True, on_delete=models.SET_NULL)
    discipline_name = models.CharField(max_length=63)
    week_day = models.DateField()
    periodicity = models.CharField(max_length=3)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


# Аудитория
class Room(models.Model):
    number = models.PositiveIntegerField()
    type_room = models.CharField(max_length=31)
    capacity = models.PositiveIntegerField()
    corps_index = models.CharField(max_length=7)
    corps_number = models.PositiveIntegerField()
