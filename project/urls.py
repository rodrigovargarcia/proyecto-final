"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib import admin
from django.urls import path
from ejemplo.views import (index, sumar, monstrar_familiares, BuscarFamiliar, AltaFamiliar, 
                            ActualizarFamiliar, BorrarFamiliar, FamiliarDetalle, FamiliarList,
                            FamiliarCrear, FamiliarBorrar, FamiliarActualizar, MascotaList, 
                            MascotaCrear, MascotaDetalle, MascotaBorrar, MascotaActualizar, 
                            AutomovilList, AutomovilCrear, AutomovilDetalle, AutomovilBorrar, 
                            AutomovilActualizar)         
from blog_app.views import (index, PostDetalle, PostListar, PostCrear, PostBorrar, PostActualizar,
                            UserSignUp, UserLogin, UserLogout, AvatarActualizar, UserActualizar,
                            MensajeCrear, MensajeListar, MensajeDetalle, MensajeBorrar)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', index),
    path('sumar/<int:a>/<int:b>', sumar),
    path('mi-familia/', monstrar_familiares),
    path('mi-familia/buscar', BuscarFamiliar.as_view()),
    path('mi-familia/alta', AltaFamiliar.as_view()),
    path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()),
    path('mi-familia/borrar/<int:pk>', BorrarFamiliar.as_view()),
    path('panel-familia/<int:pk>/detalle', FamiliarDetalle.as_view()),
    path('panel-familia/', FamiliarList.as_view()),
    path('panel-familia/crear', FamiliarCrear.as_view()),
    path('panel-familia/<int:pk>/borrar', FamiliarBorrar.as_view()),
    path('panel-familia/<int:pk>/actualizar', FamiliarActualizar.as_view()),
    path('panel-mascota/', MascotaList.as_view()),
    path('panel-mascota/crear', MascotaCrear.as_view()),
    path('panel-mascota/<int:pk>/detalle', MascotaDetalle.as_view()),
    path('panel-mascota/<int:pk>/borrar', MascotaBorrar.as_view()),
    path('panel-mascota/<int:pk>/actualizar', MascotaActualizar.as_view()),
    path('panel-automovil/', AutomovilList.as_view()),
    path('panel-automovil/crear', AutomovilCrear.as_view()),
    path('panel-automovil/<int:pk>/detalle', AutomovilDetalle.as_view()),
    path('panel-automovil/<int:pk>/borrar', AutomovilBorrar.as_view()),
    path('panel-automovil/<int:pk>/actualizar', AutomovilActualizar.as_view()),
    path('blog-app/', index, name="blog-app-index"),
    path('blog-app/listar/', PostListar.as_view(), name="blog-app-listar"),
    path('blog-app/<int:pk>/detalle/', PostDetalle.as_view(), name="blog-app-detalle"),
    path('blog-app/listar/', PostListar.as_view(), name="blog-app-listar"),
    path('blog-app/crear/', PostCrear.as_view(), name="blog-app-crear"),
    path('blog-app/<int:pk>/borrar/', PostBorrar.as_view(), name="blog-app-borrar"),
    path('blog-app/<int:pk>/actualizar/', PostActualizar.as_view(), name="blog-app-actualizar"),
    path('blog-app/signup/', UserSignUp.as_view(), name = "blog-app-signup"),
    path('blog-app/login/', UserLogin.as_view(), name = "blog-app-login"),
    path('blog-app/logout/', UserLogout.as_view(), name = "blog-app-logout"),
    path('blog-app/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name = "blog-app-avatars-actualizar"),
    path('blog-app/users/<int:pk>/actualizar/', UserActualizar.as_view(), name = "blog-app-users-actualizar"),
    path('blog-app/users/mensajes/crear/', MensajeCrear.as_view(), name = "blog-app-mensajes-crear"),
    path('blog-app/users/<int:pk>/detalle/', MensajeDetalle.as_view(), name = "blog-app-mensajes-detalle"),
    path('blog-app/users/mensajes/listar/', MensajeListar.as_view(), name = "blog-app-mensajes-listar"),
    path('blog-app/users/<int:pk>/borrar/', MensajeBorrar.as_view(), name = "blog-app-mensajes-borrar"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

