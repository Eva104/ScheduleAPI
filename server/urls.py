from rest_framework import routers
from server import views
from django.contrib import admin
from django.urls import path

router = routers.DefaultRouter()
router.register(r'Teacher', views.TeacherViewSet)
router.register(r'Chair', views.ChairViewSet)
router.register(r'Work_time', views.Work_timeViewSet)
router.register(r'Faculty', views.FacultyViewSet)
router.register(r'Direction', views.DirectionViewSet)
router.register(r'Group', views.GroupViewSet)
router.register(r'Subgroup', views.SubgroupViewSet)
router.register(r'Exam_schedule', views.Exam_scheduleViewSet)
router.register(r'Class_schedule', views.Class_scheduleViewSet)
router.register(r'Room', views.RoomViewSet)

# from server.views import TeacherViewSet


urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += router.urls

# path('', TeacherViewSet.as_view({'get': 'retrieve'}), name='teachers'),
