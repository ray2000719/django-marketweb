from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.utils import timezone
import os
from .models import production
from .forms import ProductForm

def validate_file_extension(value):
    valid_extensions = ['.gif', '.jpg', '.png']
    ext = os.path.splitext(value)[1]
    if(ext in valid_extensions):
        return True
    else:
        return False

# Create your views here.
def index(request):
    product = production.objects.all().values()
    template = loader.get_template('index.html')

    if('searchtxt' in request.GET):
        product = production.objects.filter(pname__contains = request.GET['searchtxt'])
    elif('all' in request.GET):
        product = production.objects.all().values()
    elif('vegetable' in request.GET):
        product = production.objects.filter(ptype = "蔬菜")
    elif('fruit' in request.GET):
        product = production.objects.filter(ptype = "水果")
    elif('meat' in request.GET):
        product = production.objects.filter(ptype = "肉類")
    elif('egg' in request.GET):
        product = production.objects.filter(ptype = "蛋類")
    return HttpResponse(template.render({'pdList' : product}, request))

def addPD(request):
    template = loader.get_template('addPD.html')
    
    if('post' in request.GET):

        pname = request.POST['pname']
        ptype = request.POST['ptype']

        try:
            request.FILES['pimg']
        except:
            product = production(pimg = '', pname = pname, ptype = ptype, pub_date = timezone.now())
        else:
            if(validate_file_extension(str(request.FILES['pimg']))):
                pimg = request.FILES['pimg']
                product = production(pimg = pimg, pname = pname, ptype = ptype, pub_date = timezone.now())
                product.save()
                return HttpResponseRedirect(reverse('index'))
            else:
                product = production(pimg = '', pname = pname, ptype = ptype, pub_date = timezone.now())

        return HttpResponse(template.render({'product' : product}, request))

    elif('cancel' in request.GET):
        return HttpResponseRedirect(reverse('index'))
        
    return HttpResponse(template.render({}, request))

def deletePD(request, id):
    product = production.objects.get(id=id)
    if(os.path.isfile("/marketAPP/myWeb/media/" + str(product.pimg))):
        os.remove("/marketAPP/myWeb/media/" + str(product.pimg))
    else:
        print("no data")
    product.delete()
    return HttpResponseRedirect(reverse('index'))

def updatePD(request, id):
    template = loader.get_template('addPD.html')
    product = production.objects.get(id=id)

    if('post' in request.GET):

        pname = request.POST['pname']
        ptype = request.POST['ptype']

        try:
            request.FILES['pimg']
        except:
            product = production(pimg = '', pname = pname, ptype = ptype, pub_date = timezone.now())
        else:
            if(validate_file_extension(str(request.FILES['pimg']))):
                if(os.path.isfile("/marketAPP/myWeb/media/" + str(product.pimg))):
                    os.remove("/marketAPP/myWeb/media/" + str(product.pimg))
                else:
                    print("no data")

                product.pimg = request.FILES['pimg']
                product.pname = request.POST['pname']
                product.ptype = request.POST['ptype']
                product.pub_date = timezone.now()
                product.save()

                return HttpResponseRedirect(reverse('index'))
            else:
                product = production(pimg = '', pname = pname, ptype = ptype, pub_date = timezone.now())

        return HttpResponse(template.render({'product' : product}, request))

    elif('cancel' in request.GET):
        return HttpResponseRedirect(reverse('index'))

    return HttpResponse(template.render({'product' : product}, request))