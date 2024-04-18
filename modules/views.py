from rest_framework import serializers
from rest_framework import viewsets, mixins
from .models import Module

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'


class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

class EnrollmentViewSet(mixins.ListModelMixin, 
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Module

class ModuleListView(ListView):
    model = Module 

class ModuleDetailView(DetailView):
    model = Module

class ModuleCreateView(CreateView):
    model = Module
    fields = '__all__'

class ModuleUpdateView(UpdateView):
    model = Module
    fields = '__all__'

class ModuleDeleteView(DeleteView):
    model = Module
    success_url = reverse_lazy('module_list')  # Redirect to Module list after deletion
