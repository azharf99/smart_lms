from rest_framework import serializers
from rest_framework import viewsets, mixins
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class EnrollmentViewSet(mixins.ListModelMixin, 
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Category

class CategoryListView(ListView):
    model = Category 

class CategoryDetailView(DetailView):
    model = Category

class CategoryCreateView(CreateView):
    model = Category
    fields = '__all__'

class CategoryUpdateView(UpdateView):
    model = Category
    fields = '__all__'

class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('category_list')  # Redirect to Category list after deletion
