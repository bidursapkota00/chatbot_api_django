from django.http import HttpResponse
from rest_framework import generics
from .models import Input
from .serializers import InputSerializer
from .serializers import IdSerializer
from django.views.generic import TemplateView

from django.shortcuts import get_object_or_404
from .ai import *

from rest_framework import viewsets
from rest_framework import mixins


class Api(generics.RetrieveUpdateAPIView):
    queryset = Input.objects.all()
    serializer_class = InputSerializer




class Id(generics.ListAPIView, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    # input_data = get_object_or_404(Input, id = 1)
    # # print(input_data.input)
    # output = ml(input_data.input)
    # print(output)
    # input_data.output = output
    # input_data.save()
    
    serializer_class = InputSerializer
    queryset = Input.objects.all()
    

# def home_page(request):
#     return HttpResponse(<a href="{% url 'readwrite' %}">'<h1>Hello, World</h1>'</a>)

class HomePageView(TemplateView):
    template_name = 'base.html'