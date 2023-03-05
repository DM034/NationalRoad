from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import* 
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return HttpResponse("Welcome to checkHole.")

def index1(request):
    about = loader.get_template('checkhole/option.html')
    context = { }
    return HttpResponse(about.render(context, request))

def abouthole(request):
    road = Road(0,'',0,0,'',0)
    about = loader.get_template('checkhole/abouthole.html')
    context = { "roadhole" : road.getAllHole() }
    return HttpResponse(about.render(context, request))

def inserthole(request):
    road = Road(0,'',0,0,'',0)
    about = loader.get_template('checkhole/inserthole.html')
    context = { "roadhole" : road.getRoadName() }
    return HttpResponse(about.render(context, request))

def getInsertValues(request):
    start = int(request.GET['start'])
    end = int(request.GET['end'])
    longitude1 = float(request.GET['longitude1'])
    latitude1 = float(request.GET['latitude1'])
    longitude2 = float(request.GET['longitude2'])
    latitude2 = float(request.GET['latitude2'])
    note = int(request.GET['note'])
    road = int(request.GET['road'])
    largeur = int(request.GET['largeur'])

    Hole.insertHole(start,end,longitude1,latitude1,longitude2,latitude2,note,road,largeur)
    about = loader.get_template('checkhole/option.html')
    context = { }
    return HttpResponse(about.render(context, request))

def insertpop(request):
    about = loader.get_template('checkhole/insertdistpop.html')
    context = { }
    return HttpResponse(about.render(context, request))

def insertec(request):
    about = loader.get_template('checkhole/insertdistec.html')
    context = { }
    return HttpResponse(about.render(context, request))

def inserthop(request):
    about = loader.get_template('checkhole/insertdisthop.html')
    context = { }
    return HttpResponse(about.render(context, request))

def getPop(request):
    dist = int(request.GET['dist'])
    load = loader.get_template('checkhole/population.html')
    context = { "population" : Hole.getPopulation(dist)}
    return HttpResponse(load.render(context,request))

def getEc(request):
    dist = int(request.GET['dist'])
    load = loader.get_template('checkhole/ecole.html')
    context = { "ecole" : Hole.getEcole(dist)}
    return HttpResponse(load.render(context,request))

def getHop(request):
    dist = int(request.GET['dist'])
    load = loader.get_template('checkhole/hopital.html')
    context = { "hopital" : Hole.getHopital(dist)}
    return HttpResponse(load.render(context,request))

def rn(request):
    road = Road(0,'',0,0,'',0)
    load = loader.get_template('checkhole/prior.html')
    context = { "road" : road.getRoadName()}
    return HttpResponse(load.render(context,request))
