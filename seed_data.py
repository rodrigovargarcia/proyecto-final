from ejemplo.models import Familiar
from ejemplo.models import Mascota
Familiar(nombre="Rosario", direccion="Rio Parana 745", numero_pasaporte=123123).save()
Familiar(nombre="Alberto", direccion="Rio Parana 745", numero_pasaporte=890890).save()
Familiar(nombre="Samuel", direccion="Rio Parana 745", numero_pasaporte=345345).save()
Familiar(nombre="Florencia", direccion="Rio Parana 745", numero_pasaporte=567567).save()
Mascota(raza="BorderCollie", edad=5).save()
Mascota(raza="Labrador", edad=3).save()
Mascota(raza="Pitbull", edad=7).save()
Mascota(raza="Cholo", edad=15).save()

print("Se cargo con éxito los usuarios de pruebas")