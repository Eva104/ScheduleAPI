# Generated by Django 3.2.2 on 2021-05-16 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=31, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Кафедра',
                'verbose_name_plural': 'Кафедры',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('code', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='Код направления')),
                ('name', models.CharField(max_length=31, verbose_name='Название')),
                ('qualification', models.CharField(max_length=63, verbose_name='Квалификация')),
                ('chair', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='server.chair', verbose_name='Кафедра')),
            ],
            options={
                'verbose_name': 'Направление',
                'verbose_name_plural': 'Направления',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=31, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Факультет',
                'verbose_name_plural': 'Факультеты',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=31, verbose_name='Группа')),
                ('amount', models.PositiveIntegerField(verbose_name='Количество')),
                ('direction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='server.direction', verbose_name='Направление')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(verbose_name='Номер')),
                ('type_room', models.CharField(max_length=31, verbose_name='Тип аудитории')),
                ('capacity', models.PositiveIntegerField(verbose_name='Ёмкость')),
                ('corps_index', models.CharField(max_length=7, verbose_name='Индекс корпуса')),
                ('corps_number', models.PositiveIntegerField(verbose_name='Номер корпуса')),
            ],
            options={
                'verbose_name': 'Аудитория',
                'verbose_name_plural': 'Аудитории',
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=31, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=31, verbose_name='Имя')),
                ('patronymic', models.CharField(max_length=31, verbose_name='Отчество')),
                ('position', models.CharField(max_length=31, verbose_name='Должность')),
                ('rate', models.FloatField(default=None, null=True, verbose_name='Ставка')),
                ('hours', models.PositiveIntegerField(default=None, null=True, verbose_name='Количество рабочих часов')),
                ('chair', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='server.chair', verbose_name='Кафедра')),
            ],
            options={
                'verbose_name': 'Преподаватель',
                'verbose_name_plural': 'Преподаватели',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Work_time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday_start', models.TimeField(blank=True, null=True, verbose_name='Понедельник - начало')),
                ('monday_end', models.TimeField(blank=True, null=True, verbose_name='Понедельник - конец')),
                ('tuesday_start', models.TimeField(blank=True, null=True, verbose_name='Вторник - начало')),
                ('tuesday_end', models.TimeField(blank=True, null=True, verbose_name='Вторник - конец')),
                ('wednesday_start', models.TimeField(blank=True, null=True, verbose_name='Среда - начало')),
                ('wednesday_end', models.TimeField(blank=True, null=True, verbose_name='Среда - конец')),
                ('thursday_start', models.TimeField(blank=True, null=True, verbose_name='Четверг - начало')),
                ('thursday_end', models.TimeField(blank=True, null=True, verbose_name='Четверг - конец')),
                ('friday_start', models.TimeField(blank=True, null=True, verbose_name='Пятница - начало')),
                ('friday_end', models.TimeField(blank=True, null=True, verbose_name='Пятница - конец')),
                ('saturday_start', models.TimeField(blank=True, null=True, verbose_name='Суббота - начало')),
                ('saturday_end', models.TimeField(blank=True, null=True, verbose_name='Суббота - конец')),
                ('corps_index', models.CharField(max_length=7)),
                ('corps_number', models.PositiveIntegerField()),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='server.teacher')),
            ],
            options={
                'verbose_name': 'Рабочее время преподавателей',
                'verbose_name_plural': 'Рабочее время преподавателя',
            },
        ),
        migrations.CreateModel(
            name='Subgroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(verbose_name='Номер подгруппы')),
                ('amount', models.PositiveIntegerField(verbose_name='Количество')),
                ('group_parent', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='server.group', verbose_name='Родительская группа')),
            ],
            options={
                'verbose_name': 'Подгруппа',
                'verbose_name_plural': 'Подгруппы',
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='Exam_schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63, verbose_name='Название')),
                ('date', models.DateField(verbose_name='Дата экзамена')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='server.group')),
            ],
            options={
                'verbose_name': 'Расписание экзамена',
                'verbose_name_plural': 'Расписание экзаменов',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Class_schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discipline_name', models.CharField(max_length=63, verbose_name='Дисциплина')),
                ('week_day', models.CharField(max_length=31, verbose_name='День недели')),
                ('periodicity', models.CharField(max_length=7, verbose_name='Частота')),
                ('start_time', models.TimeField(verbose_name='Начало')),
                ('end_time', models.TimeField(verbose_name='Конец')),
                ('groups', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='server.group', verbose_name='Группы')),
                ('room', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='server.room', verbose_name='Аудитория')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='server.teacher', verbose_name='Преподаватель')),
            ],
            options={
                'verbose_name': 'Расписание занятия',
                'verbose_name_plural': 'Расписание занятий',
                'ordering': ['room'],
            },
        ),
        migrations.AddField(
            model_name='chair',
            name='faculty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='server.faculty', verbose_name='Факультет'),
        ),
    ]
