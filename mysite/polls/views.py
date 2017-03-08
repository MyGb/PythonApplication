from django.http import HttpResponse
from django.core import serializers
import json
from .models import Job
# Create your views here.

def index(request):
	result = Job.objects.all()
	data = serializers.serialize('json', result)
	return HttpResponse(data)