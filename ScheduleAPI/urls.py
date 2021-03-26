from django.urls import include, path
from rest_framework import routers
from ScheduleAPI import views

# router = routers.DefaultRouter()
# router.register(r'Teacher', views.TeacherSet)
# router.register(r'Chair', views.ChairSet)
# router.register(r'Work_time', views.Work_timeSet)
# router.register(r'Faculty', views.FacultySet)
# router.register(r'Direction', views.DirectionSet)
# router.register(r'Group', views.GroupSet)
# router.register(r'Subgroup', views.SubgroupSet)
# router.register(r'Exam_schedule', views.Exam_scheduleSet)
# router.register(r'Class_schedule', views.Class_scheduleSet)
# router.register(r'Room', views.RoomSet)
from ScheduleAPI.views import TeacherViewSet

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', TeacherViewSet.as_view({'get': 'retrieve'}), name = 'teachers' ),

]