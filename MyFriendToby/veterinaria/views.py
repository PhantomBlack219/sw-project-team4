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
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from random import choice
from .models import *
from .forms import *

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

def servicesView(request):
    template = loader.get_template('services.html')
    context = {}
    return HttpResponse(template.render(context,request))

def loginView(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
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
            return redirect('login')
    else:
        return render(request, 'Login.html')

def selectCreateTypeAccountView(request):
    template = loader.get_template('SelectCreateAccountType.html')
    context = {}
    return HttpResponse(template.render(context,request))



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
            return redirect('createuserform')
    else:
        return render(request, 'CreateUserForm.html')

def mascotasView(request):
     # Filtra las mascotas por el campo adoptado
    mascotas = Mascota.objects.filter(adoptado=False)
    return render(request, 'Mascotas.html', {'mascotas': mascotas})

@login_required
def TusMascotasView(request):
    # # Asegúrate de que el usuario esté autenticado
    if request.user.is_authenticated:
        # Filtra las mascotas por el id_adoptante si el usuario pertenece al grupo "adoptante"
        if request.user.groups.filter(name='adoptante').exists():
            mascotas = Mascota.objects.filter(id_adoptante=request.user)
        # Filtra las mascotas por el id_veterinario si el usuario pertenece al grupo "veterinario"
        elif request.user.groups.filter(name='veterinario').exists():
            mascotas = Mascota.objects.filter(id_veterinario=request.user)
        else:
            mascotas = Mascota.objects.filter(id_donante=request.user)
        return render(request, 'TusMascotas.html', {'mascotas': mascotas})
    else:
        return redirect('login')


def add_petForm(request):
    if request.method == 'POST':
        form = AddPetForm(request.POST)
        if form.is_valid():
            new_pet = form.save()
            # Asegurarse de que el usuario autenticado pertenece al grupo 'donante'
            if request.user.groups.filter(name='donante').exists():
                new_pet.id_donante = request.user
            else:
                return redirect('login')  # Redirige a una página de error si el usuario no es un donante

            # Asignar un veterinario aleatorio del grupo 'veterinario'
            vet_group = Group.objects.get(name='veterinario')
            vets = vet_group.user_set.all()
            if vets:
                new_pet.id_veterinario = choice(vets)
            else:
                return redirect('login')  # Redirige a una página de error si no hay veterinarios

            new_pet.save()
            return redirect('Tus_mascotas')  # Redirige a la lista de mascotas después de un envío exitoso
    else:
        form = AddPetForm()

    return render(request, 'AddPetForm.html', {'form': form})


def edit_petForm(request, id):
    if request.method == 'POST':
        mascota = Mascota.objects.get(pk=id)
        mascota.adoptado = False  
        if 'adoptado' in request.POST:  
            mascota.adoptado = True
        mascota.nombre = request.POST.get('nombre')
        mascota.edad = request.POST.get('edad')
        mascota.peso = request.POST.get('peso')
        mascota.tamaño = request.POST.get('tamaño')
        mascota.save()
        return redirect('Tus_mascotas')
    else:
        mascota = Mascota.objects.get(pk=id)
        return render(request, 'EditPetCard.html', {'mascota': mascota})

def edit_petVetForm(request, id):
    mascota = Mascota.objects.get(pk=id)
    if request.method == 'POST':
        mascota.adoptado = False  
        if 'adoptado' in request.POST:  
            mascota.adoptado = True
        mascota.nombre = request.POST.get('nombre')
        mascota.edad = request.POST.get('edad')
        mascota.peso = request.POST.get('peso')
        mascota.tamaño = request.POST.get('tamaño')
        mascota.enfermedades = request.POST.get('enfermedades')
        mascota.dineromantenimiento = request.POST.get('dineromantenimiento')
        mascota.espaciomantenimiento = request.POST.get('espaciomantenimiento')
        mascota.chequeo = request.POST.get('chequeo')
        mascota.prox_chequeo = request.POST.get('prox_chequeo')
        mascota.save()
        return redirect('Tus_mascotas')
    else:
        return render(request, 'EditPetCardVet.html', {'mascota': mascota})


def eliminar_mascota(request, id):
    if request.method == 'POST':
        mascota = Mascota.objects.get(pk=id)
        mascota.delete()
        return redirect('Tus_mascotas')


#def adopt_petForm(request, id):
    #if request.method == 'POST':
        #form = FormularioAdopcionForm(request.POST)
        #if form.is_valid():
            #formulario = form.save(commit=False)
            #formulario.usuario = request.user
            #formulario.mascota = Mascota.objects.get(pk=id)
            #formulario.save()

            #mascota = Mascota.objects.get(pk=id)
            #mascota.id_adoptante = request.user
            #mascota.save()

            #return redirect('Tus_mascotas')
    #else:
        #form = FormularioAdopcionForm()
        #mascota = Mascota.objects.get(pk=id)

   #return render(request, 'AdoptPetCard.html', {'form': form})


from .models import Mascota, FormularioAdopcion

def adopt_petForm(request, id):
    if request.method == 'POST':
        form = FormularioAdopcionForm(request.POST)
        mascota = Mascota.objects.get(pk=id)
        if form.is_valid():
            new_pet = form.save(commit=False)
            new_pet.usuario = request.user
            new_pet.mascota = mascota  # Asigna la instancia de la mascota, no el ID
            new_pet.save()
            
            mascota.adoptado = True
            mascota.id_adoptante = request.user
            mascota.save()
            
            return redirect('Tus_mascotas')  # Redirige a la lista de mascotas después de un envío exitoso
    else:
        form = FormularioAdopcionForm()

    return render(request, 'AdoptPetCard.html', {'form': form})


