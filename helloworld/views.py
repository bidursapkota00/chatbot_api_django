from rest_framework import generics
from .models import Input
from .serializers import InputSerializer
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .ai import *
from rest_framework import mixins


# class Api(mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Input.objects.all()
#     serializer_class = InputSerializer

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
@api_view(['POST'])
def api(request):
    serializer = InputSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        ip = [ip.input for ip in Input.objects.all()]
        op = ml(ip[-1])
        i = [ip for ip in Input.objects.all()]
        i[-1].output = op
        i[-1].save()
        return Response({"output": op})

    return Response({"success":"false"})      

class Id(APIView):
    def get(self,request,format=json):
        ip = [ip.input for ip in Input.objects.all()]
        op = ml(ip[-1])
        i = [ip for ip in Input.objects.all()]
        i[-1].output = op
        i[-1].save()
        return Response({"output": op})
    

class HomePageView(TemplateView):
    template_name = 'base.html'