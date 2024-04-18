from rest_framework import serializers
from rest_framework import viewsets, mixins
from .models import Submission

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'


class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

class EnrollmentViewSet(mixins.ListModelMixin, 
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer



from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Submission

class SubmissionListView(ListView):
    model = Submission 

class SubmissionDetailView(DetailView):
    model = Submission

class SubmissionCreateView(CreateView):
    model = Submission
    fields = '__all__'

class SubmissionUpdateView(UpdateView):
    model = Submission
    fields = '__all__'

class SubmissionDeleteView(DeleteView):
    model = Submission
    success_url = reverse_lazy('submission_list')  # Redirect to Submission list after deletion
