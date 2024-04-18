from rest_framework import serializers
from rest_framework import viewsets, mixins
from .models import Grade

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

class EnrollmentViewSet(mixins.ListModelMixin, 
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Grade

class GradeListView(ListView):
    model = Grade 

class GradeDetailView(DetailView):
    model = Grade

class GradeCreateView(CreateView):
    model = Grade
    fields = '__all__'

class GradeUpdateView(UpdateView):
    model = Grade
    fields = '__all__'

class GradeDeleteView(DeleteView):
    model = Grade
    success_url = reverse_lazy('grade_list')  # Redirect to course list after deletion
