from rest_framework import serializers
from rest_framework import viewsets, mixins
from .models import Quiz

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class EnrollmentViewSet(mixins.ListModelMixin, 
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Quiz

class QuizListView(ListView):
    model = Quiz 

class QuizDetailView(DetailView):
    model = Quiz

class QuizCreateView(CreateView):
    model = Quiz
    fields = '__all__'

class QuizUpdateView(UpdateView):
    model = Quiz
    fields = '__all__'

class QuizDeleteView(DeleteView):
    model = Quiz
    success_url = reverse_lazy('quiz_list')  # Redirect to Quiz list after deletion
