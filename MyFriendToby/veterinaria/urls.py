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
    path('mascotas/', views.mascotasView, name='mascotas'),
    path('Añadir_mascota/', views.add_petForm, name='añadir_mascotas'),
    path('accounts/login/', views.loginView, name='login'),
    path('accounts/login/selectcreateaccounttype', views.selectCreateTypeAccountView, name='selectcreateaccounttype'),
    path('accounts/login/selectcreateaccounttype/createvetform/', views.createVetForm, name='createvetform'),
    path('accounts/login/selectcreateaccounttype/createuserform/', views.createUserForm, name='createuserform')       
]