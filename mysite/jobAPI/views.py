#from django.shortcuts import render

# Create your views here.
from .models import Job
from rest_framework import viewsets
from .serializers import JobSerializer

class JobViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer