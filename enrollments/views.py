from rest_framework import serializers
from rest_framework import viewsets, mixins
from .models import Enrollment

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class EnrollmentViewSet(mixins.ListModelMixin, 
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Enrollment

class EnrollmentListView(ListView):
    model = Enrollment 

class EnrollmentDetailView(DetailView):
    model = Enrollment

class EnrollmentCreateView(CreateView):
    model = Enrollment
    fields = '__all__'

class EnrollmentUpdateView(UpdateView):
    model = Enrollment
    fields = '__all__'

class EnrollmentDeleteView(DeleteView):
    model = Enrollment
    success_url = reverse_lazy('enrollment_list')  # Redirect to course list after deletion
