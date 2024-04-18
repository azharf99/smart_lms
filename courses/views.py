from rest_framework import serializers
from rest_framework import viewsets, mixins
from django.contrib.auth.models import User
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class EnrollmentViewSet(mixins.ListModelMixin, 
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EnrollmentViewSet(mixins.ListModelMixin, 
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Course

class CourseListView(ListView):
    model = Course 

class CourseDetailView(DetailView):
    model = Course

class CourseCreateView(CreateView):
    model = Course
    fields = '__all__'

class CourseUpdateView(UpdateView):
    model = Course
    fields = '__all__'

class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('course_list')  # Redirect to course list after deletion


class UserListView(ListView):
    model = User 

class UserDetailView(DetailView):
    model = User

class UserCreateView(CreateView):
    model = User
    fields = '__all__'

class UserUpdateView(UpdateView):
    model = User
    fields = '__all__'

class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('user_list')  # Redirect to course list after deletion
