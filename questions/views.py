from rest_framework import serializers
from rest_framework import viewsets, mixins
from .models import Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class EnrollmentViewSet(mixins.ListModelMixin, 
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Question

class QuestionListView(ListView):
    model = Question 

class QuestionDetailView(DetailView):
    model = Question

class QuestionCreateView(CreateView):
    model = Question
    fields = '__all__'

class QuestionUpdateView(UpdateView):
    model = Question
    fields = '__all__'

class QuestionDeleteView(DeleteView):
    model = Question
    success_url = reverse_lazy('question_list')  # Redirect to Question list after deletion
