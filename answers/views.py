from rest_framework import serializers
from rest_framework import viewsets, mixins
from .models import Answer

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class EnrollmentViewSet(mixins.ListModelMixin, 
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Answer

class AnswerListView(ListView):
    model = Answer 

class AnswerDetailView(DetailView):
    model = Answer

class AnswerCreateView(CreateView):
    model = Answer
    fields = '__all__'

class AnswerUpdateView(UpdateView):
    model = Answer
    fields = '__all__'

class AnswerDeleteView(DeleteView):
    model = Answer
    success_url = reverse_lazy('answer_list')  # Redirect to Answer list after deletion
