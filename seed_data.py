from ejemplo.models import Familiar
from ejemplo.models import Mascota
from ejemplo.models import Automovil

Familiar(nombre="Rosario", direccion="Rio Parana 745", numero_pasaporte=123123).save()
Familiar(nombre="Alberto", direccion="Rio Parana 745", numero_pasaporte=890890).save()
Familiar(nombre="Samuel", direccion="Rio Parana 745", numero_pasaporte=345345).save()
Familiar(nombre="Florencia", direccion="Rio Parana 745", numero_pasaporte=567567).save()
Mascota(raza="BorderCollie", edad=5).save()
Mascota(raza="Labrador", edad=3).save()
Mascota(raza="Pitbull", edad=7).save()
Mascota(raza="Cholo", edad=15).save()
Automovil(marca="Volkswagen", modelo="Amarok", año=2016, km=101300).save()
Automovil(marca="Peugeot", modelo="208", año=2016, km=80500).save()
Automovil(marca="Toyota", modelo="Etios", año=2014, km=105300).save()
Automovil(marca="Volkswagen", modelo="Up", año=2020, km=10300).save()
Automovil(marca="Chevrolet", modelo="Cruze", año=2018, km=15500).save()
print("Se cargo con éxito los usuarios de pruebas")