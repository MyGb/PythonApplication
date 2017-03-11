from django.http import HttpResponse
from django.db.models import Count
from .models import Job
import json
# Create your views here.

def index(request):
	#select industryfield,count(industryfield) from job group by industryfield
	groupResult = Job.objects.values("industryfield").annotate(total=Count("industryfield"))
	total = Job.objects.count()
	info = (r for r in groupResult)
	data = {"total":total,"info":list(info)}
	jsonData = {"code":0,"message":"success","total":total,"data":data}
	return HttpResponse(json.dumps(jsonData))