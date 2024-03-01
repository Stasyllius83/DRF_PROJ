from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics
from materials.paginators import CoursePagination, LessonPagination
from materials.permissions import IsOwner, IsStaff
from materials.models import Course, Lesson, Subscription
from rest_framework.permissions import IsAuthenticated
from materials.serializers import CourseSerializer, LessonSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = []
    pagination_class = CoursePagination

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated, ~IsStaff]
        elif self.action == 'list':
            self.permission_classes = [IsAuthenticated, IsOwner|IsStaff]
        elif self.action == 'retrieve':
            self.permission_classes = [IsAuthenticated, IsOwner|IsStaff]
        elif self.action == 'update':
            self.permission_classes = [IsAuthenticated, IsOwner|IsStaff]
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, IsOwner]
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsStaff]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner|IsStaff]
    pagination_class = LessonPagination


class LessonRetrieveView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner|IsStaff]


class LessonUpdateView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner|IsStaff]


class LessonDestroyView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class SubscriptionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data["course"]
        course_item = get_object_or_404(Course, pk=course_id)

        subs_item, created = Subscription.objects.update_or_create(course=course_item, user=user)

        if created:
            subs_item.status_subscrip = True
            subs_item.save()
            message = 'подписка добавлена'
        # Если подписка у пользователя на этот курс есть - удаляем ее
        elif subs_item.status_subscrip:
            subs_item.status_subscrip = False
            subs_item.save()
            message = 'подписка удалена'

        else:
        # Если подписки у пользователя на этот курс нет - создаем ее
            subs_item.status_subscrip = True
            subs_item.save()
            message = 'подписка добавлена'

        # Возвращаем ответ в API
        return Response({"message": message})
