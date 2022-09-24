from django.http import HttpResponse
from django.template import loader
from .models import Test

def index(request):
  p = Test.objects.all().values()
  template = loader.get_template('myfirst.html')
  context = {
    'pp' : p,
  }
  return HttpResponse(template.render(context, request))

def indexx(request):
  return HttpResponse("Hello world!")