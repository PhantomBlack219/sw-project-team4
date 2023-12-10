from unicodedata import name
from django.urls import path
from django.views import View


from . import views 

urlpatterns = [
    path('', views.indexView, name='index'),
    path('blog/', views.blogView, name='blog'),
    path('blog_details/', views.blog_detailsView, name='blog_details'),
    path('about/', views.aboutView, name='about'),
    path('contact/', views.contactView, name='contact'),
    path('Tus_mascotas/', views.TusMascotasView, name='Tus_mascotas'),
    path('Tus_mascotas/editar_mascota/<id>/', views.edit_petForm, name='editar_mascotas'),
    path('Tus_mascotas/eliminar_mascota/<id>/', views.eliminar_mascota, name='eliminar_mascotas'),
    path('Tus_mascotas/editar_mascota_vet/<id>/', views.edit_petVetForm, name='editar_mascotas_vet'),
    path('mascotas/', views.mascotasView, name='mascotas'),
    path('mascotas/adoptar_mascota/<id>/', views.adopt_petForm, name='adoptar_mascotas'),
    
    path('Añadir_mascota/', views.add_petForm, name='añadir_mascotas'),
    path('accounts/login/', views.loginView, name='login'),
    path('accounts/login/selectcreateaccounttype', views.selectCreateTypeAccountView, name='selectcreateaccounttype'),
    path('accounts/login/selectcreateaccounttype/createvetform/', views.createVetForm, name='createvetform'),
    path('accounts/login/selectcreateaccounttype/createuserform/', views.createUserForm, name='createuserform')       
]