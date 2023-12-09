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
    path('elements/', views.elementsView, name='elements'),
    path('Tus_mascotas/', views.TusMascotasView, name='mascotas'),
    path('accounts/login/', views.loginView, name='login'),
    path('accounts/login/selectcreateaccounttype', views.selectCreateTypeAccountView, name='selectcreateaccounttype'),
    path('accounts/login/selectcreateaccounttype/createvetform/', views.createVetForm, name='createvetform'),
    path('accounts/login/selectcreateaccounttype/createuserform/', views.createUserForm, name='createuserform')       
]