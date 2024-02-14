from django.urls import path
from materials.apps import MaterialsConfig
from rest_framework.routers import DefaultRouter

from materials.views import CourseViewSet, LessonCreateAPIView, LessonDestroyView, LessonListAPIView, LessonRetrieveView, LessonUpdateView

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')


urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/<int:pk>/', LessonRetrieveView.as_view(), name='lesson-get'),
    path('lesson/update/<int:pk>/', LessonUpdateView.as_view(), name='lesson-update'),
    path('lesson/delete/<int:pk>/', LessonDestroyView.as_view(), name='lesson-delete')
] + router.urls
