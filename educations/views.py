from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from educations.models import Course, Lesson
from educations.serializers import CourseSerializer, LessonSerializer
from users.permissions import IsModer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsAdminUser,)

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = (IsAdminUser, )
        elif self.action == 'update':
            self.permission_classes = (IsModer | IsAdminUser,)
        elif self.action == 'retrieve':
            self.permission_classes = (IsModer | IsAdminUser,)
        elif self.action == 'list':
            self.permission_classes = (IsModer | IsAdminUser, )
        elif self.action == 'destroy':
            self.permission_classes = (IsAdminUser,)
        return super().get_permissions()

class LessonListAPIView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsModer | IsAdminUser)


class LessonCreateAPIView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAdminUser,)


class LessonRetrieveAPIView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsModer | IsAdminUser)

class LessonUpdateAPIView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsModer | IsAdminUser)


class LessonDestroyAPIViews(DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = LessonSerializer
