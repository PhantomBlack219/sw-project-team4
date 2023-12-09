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
from django.urls import reverse
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login

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

def loginView(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Django's built-in User model doesn't have an email field as the unique identifier, it uses username.
        # So, if you are using Django's built-in User model, you need to get the username from the email.
        # If you are using a custom User model with email as the unique identifier, you can skip this step.
        try:
            username = User.objects.get(email=email).username
        except User.DoesNotExist:
            username = None

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            # Aquí puedes manejar el error como desees, por ejemplo, puedes registrar el error en tus logs
            return redirect('Login.html')
    else:
        return render(request, 'Login.html')

def selectCreateTypeAccountView(request):
    template = loader.get_template('SelectCreateAccountType.html')
    context = {}
    return HttpResponse(template.render(context,request))

def devolverALogin(request):
    # ... lógica de tu vista ...
    # En el lugar donde decides que quieres redirigir, puedes usar el siguiente código:
    return redirect(reverse('login'))

def createVetForm(request):
    template = loader.get_template('CreateVetForm.html')
    context = {}
    return HttpResponse(template.render(context,request))

def createUserForm(request):
    
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
            first_name = request.POST['name']
            last_name = request.POST['lastname']
            # Aquí puedes agregar los campos adicionales de tu formulario

            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                # Obtener el tipo de usuario del formulario
            user_type = request.POST['user_type']
            user.save()
            # Buscar el grupo correspondiente
            group = Group.objects.get(name=user_type)

            # Agregar el usuario al grupo
            user.groups.add(group)
            

            return redirect('index')
        except:
            # Aquí puedes manejar el error como desees, por ejemplo, puedes registrar el error en tus logs
            return redirect('CreateUserForm.html')
    else:
        return render(request, 'CreateUserForm.html')

def TusMascotasView(request):
    template = loader.get_template('mascotas.html')
    context = {}
    return HttpResponse(template.render(context,request))