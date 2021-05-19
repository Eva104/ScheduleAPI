from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    task = models.CharField(max_length=255)
    owner = models.ForeignKey(User, related_name="todos", on_delete=models.CASCADE, null=True)  # added
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task


# Преподаватель
class Teacher(models.Model):
    surname = models.CharField(max_length=31, verbose_name='Фамилия')
    name = models.CharField(max_length=31, verbose_name='Имя')
    patronymic = models.CharField(max_length=31, verbose_name='Отчество')
    position = models.CharField(max_length=31, verbose_name='Должность')
    chair = models.ForeignKey('Chair', null=True, on_delete=models.SET_NULL, verbose_name='Кафедра')
    rate = models.FloatField(null=True, default=None, verbose_name='Ставка')
    hours = models.PositiveIntegerField(default=None, null=True, verbose_name='Количество рабочих часов')

    class Meta:
        verbose_name_plural = 'Преподаватели'
        verbose_name = 'Преподаватель'
        ordering = ['name']

    def __str__(self):
        return self.surname + ' ' + str(self.name)[:-len(self.name) + 1] + '.' + str(self.patronymic)[
                                                                                 :-len(self.patronymic) + 1] + '.'


# Кафедра
class Chair(models.Model):
    name = models.CharField(max_length=31, verbose_name='Название')
    faculty = models.ForeignKey('Faculty', null=True, on_delete=models.SET_NULL, verbose_name='Факультет')

    class Meta:
        verbose_name_plural = 'Кафедры'
        verbose_name = 'Кафедра'
        ordering = ['name']

    def __str__(self):
        return self.name


# Рабочее время
class Work_time(models.Model):
    teacher = models.ForeignKey('Teacher', null=True, on_delete=models.SET_NULL)
    # ! idk!
    monday_start = models.TimeField(verbose_name='Понедельник - начало', null=True, blank=True)
    monday_end = models.TimeField(verbose_name='Понедельник - конец', null=True, blank=True)
    tuesday_start = models.TimeField(verbose_name='Вторник - начало', null=True, blank=True)
    tuesday_end = models.TimeField(verbose_name='Вторник - конец', null=True, blank=True)
    wednesday_start = models.TimeField(verbose_name='Среда - начало', null=True, blank=True)
    wednesday_end = models.TimeField(verbose_name='Среда - конец', null=True, blank=True)
    thursday_start = models.TimeField(verbose_name='Четверг - начало', null=True, blank=True)
    thursday_end = models.TimeField(verbose_name='Четверг - конец', null=True, blank=True)
    friday_start = models.TimeField(verbose_name='Пятница - начало', null=True, blank=True)
    friday_end = models.TimeField(verbose_name='Пятница - конец', null=True, blank=True)
    saturday_start = models.TimeField(verbose_name='Суббота - начало', null=True, blank=True)
    saturday_end = models.TimeField(verbose_name='Суббота - конец', null=True, blank=True)

    corps_index = models.CharField(max_length=7)
    corps_number = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = 'Рабочее время преподавателя'
        verbose_name = 'Рабочее время преподавателей'

    def __str__(self):  # * Hmmm... I'm fine
        return f'Рабочее время ' + self.teacher.surname + ' ' + str(self.teacher.name)[
                                                                :-len(self.teacher.name) + 1] + '.' + str(
            self.teacher.patronymic)[:-len(self.teacher.patronymic) + 1] + '.'


# Факультет
class Faculty(models.Model):
    name = models.CharField(max_length=31, verbose_name='Название')

    class Meta:
        verbose_name_plural = 'Факультеты'
        verbose_name = 'Факультет'
        ordering = ['name']

    def __str__(self):
        return self.name


# Направление
class Direction(models.Model):
    code = models.CharField(max_length=15, primary_key=True, verbose_name='Код направления')  # id
    name = models.CharField(max_length=31, verbose_name='Название')
    chair = models.ForeignKey('Chair', null=True, on_delete=models.SET_NULL, verbose_name='Кафедра')
    qualification = models.CharField(max_length=63, verbose_name='Квалификация')

    class Meta:
        verbose_name_plural = 'Направления'
        verbose_name = 'Направление'
        ordering = ['name']

    def __str__(self):
        return self.name


# Группа
class Group(models.Model):
    name = models.CharField(max_length=31, verbose_name='Группа')
    amount = models.PositiveIntegerField(verbose_name='Количество')
    direction = models.ForeignKey('Direction', null=True, on_delete=models.SET_NULL, verbose_name='Направление')

    class Meta:
        verbose_name_plural = 'Группы'
        verbose_name = 'Группа'
        ordering = ['name']

    def __str__(self):
        return self.name


# Подгруппа
class Subgroup(models.Model):
    number = models.PositiveIntegerField(verbose_name='Номер подгруппы')
    amount = models.PositiveIntegerField(verbose_name='Количество')
    group_parent = models.OneToOneField('Group', null=True, on_delete=models.SET_NULL,
                                        verbose_name='Родительская группа')

    class Meta:
        verbose_name_plural = 'Подгруппы'
        verbose_name = 'Подгруппа'
        ordering = ['number']

    def __str__(self):
        return f'Подгруппа {self.group_parent.name} N{self.number}'


# Расписание экзамена
class Exam_schedule(models.Model):
    name = models.CharField(max_length=63, verbose_name='Название')
    date = models.DateField(verbose_name='Дата экзамена')
    group = models.ForeignKey('Group', null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = 'Расписание экзаменов'
        verbose_name = 'Расписание экзамена'
        ordering = ['name']

    def __str__(self):
        return f'{self.name} - {self.group.name}'


# Аудитория
class Room(models.Model):
    number = models.PositiveIntegerField(verbose_name='Номер')
    type_room = models.CharField(max_length=31, verbose_name='Тип аудитории')
    capacity = models.PositiveIntegerField(verbose_name='Ёмкость')
    corps_index = models.CharField(max_length=7, verbose_name='Индекс корпуса')
    corps_number = models.PositiveIntegerField(verbose_name='Номер корпуса')

    class Meta:
        verbose_name_plural = 'Аудитории'
        verbose_name = 'Аудитория'
        ordering = ['number']

    def __str__(self):
        return str(self.number)


# Расписание занятия
class Class_schedule(models.Model):
    groups = models.ForeignKey('Group', null=True, on_delete=models.SET_NULL, verbose_name='Группы')
    teacher = models.ForeignKey('Teacher', null=True, on_delete=models.SET_NULL, verbose_name='Преподаватель')
    room = models.OneToOneField('Room', null=True, on_delete=models.SET_NULL, verbose_name='Аудитория')
    discipline_name = models.CharField(max_length=63, verbose_name='Дисциплина')
    week_day = models.CharField(max_length=31,
                                verbose_name='День недели')  # * бэк должен позволить выбрать список вариантов
    periodicity = models.CharField(max_length=7, verbose_name='Частота')
    start_time = models.TimeField(verbose_name='Начало')
    end_time = models.TimeField(verbose_name='Конец')

    class Meta:
        verbose_name_plural = 'Расписание занятий'
        verbose_name = 'Расписание занятия'
        ordering = ['room']

    def __str__(self):  # * Hmmm... I'm fine
        return self.discipline_name + '. ауд.:' + str(
            self.room.number) + f' {self.room.corps_index}/{self.room.corps_number}'
