from django.http import HttpResponse,JsonResponse
from django.core import serializers
from .models import Job
# Create your views here.

def index(request):
	result = Job.objects.all().filter(financestage__contains="初创型")
	data = serializers.serialize('json', result)
	return HttpResponse(data)