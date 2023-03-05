from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index1, name='option'),
    path('abouthole', views.abouthole, name='abouthole'),
    path('inserthole', views.inserthole, name='inserthole'),
    path('vita', views.getInsertValues, name='inserthole'),
    path('insertdistpop', views.insertpop, name='insertdistpop'),
    path('population', views.getPop, name='population'),
    path('insertdisthop', views.inserthop, name='insertdisthop'),
    path('hopital', views.getHop, name='hopital'),
    path('insertdistec', views.insertec, name='insertdistEc'),
    path('ecole', views.getEc, name='ecole'),
    path('prior', views.rn, name='prior'),
]
