from multiprocessing import context
from re import template
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic.detail import DetailView
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings
from .models import *


def indexView(request):
    template = loader.get_template('index.html')
    context = {}
   
    return HttpResponse(template.render(context,request))

def aboutView(request):
    template = loader.get_template('about.html')
    context = {}
    return HttpResponse(template.render(context,request))

def blogView(request):
    template = loader.get_template('blog.html')
    context = {}
    return HttpResponse(template.render(context,request))

def blog_detailsView(request):
    template = loader.get_template('blog_details.html')
    context = {}
    return HttpResponse(template.render(context,request))

def blog_detailsView(request):
    template = loader.get_template('blog_details.html')
    context = {}
    return HttpResponse(template.render(context,request))

def contactView(request):
    template = loader.get_template('contact.html')
    context = {}
    return HttpResponse(template.render(context,request))

def elementsView(request):
    template = loader.get_template('elements.html')
    context = {}
    return HttpResponse(template.render(context,request))

def servicesView(request):
    template = loader.get_template('services.html')
    context = {}
    return HttpResponse(template.render(context,request))