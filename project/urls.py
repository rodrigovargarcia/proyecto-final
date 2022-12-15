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
from django.contrib import admin
from django.urls import path
from ejemplo.views import (index, sumar, monstrar_familiares, BuscarFamiliar, AltaFamiliar, 
                            ActualizarFamiliar, BorrarFamiliar, FamiliarDetalle, FamiliarList,
                            FamiliarCrear, FamiliarBorrar, FamiliarActualizar, MascotaList, MascotaCrear, MascotaDetalle, MascotaBorrar,
                            MascotaActualizar, AutomovilList, AutomovilCrear, AutomovilDetalle, AutomovilBorrar, AutomovilActualizar)         

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
]
