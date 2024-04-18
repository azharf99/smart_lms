from rest_framework import serializers
from rest_framework import viewsets, mixins
from .models import Content

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class EnrollmentViewSet(mixins.ListModelMixin, 
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Content

class ContentListView(ListView):
    model = Content 

class ContentDetailView(DetailView):
    model = Content

class ContentCreateView(CreateView):
    model = Content
    fields = '__all__'

class ContentUpdateView(UpdateView):
    model = Content
    fields = '__all__'

class ContentDeleteView(DeleteView):
    model = Content
    success_url = reverse_lazy('content_list')  # Redirect to Content list after deletion
