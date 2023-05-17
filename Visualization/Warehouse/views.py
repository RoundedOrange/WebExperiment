from django.http import  HttpResponse
from  .models import Item
import subprocess
# Create your views here.
def refresh(request):
    #Item.objects.all().delete()
    #subprocess.Popen('scrapy crawl maitian')

    return HttpResponse("DANGER!REQUEST DENIED!")