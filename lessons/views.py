from rest_framework import serializers
from rest_framework import viewsets, mixins
from .models import Lesson

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class EnrollmentViewSet(mixins.ListModelMixin, 
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Lesson

class LessonListView(ListView):
    model = Lesson 

class LessonDetailView(DetailView):
    model = Lesson

class LessonCreateView(CreateView):
    model = Lesson
    fields = '__all__'

class LessonUpdateView(UpdateView):
    model = Lesson
    fields = '__all__'

class LessonDeleteView(DeleteView):
    model = Lesson
    success_url = reverse_lazy('lesson_list')  # Redirect to Lesson list after deletion
