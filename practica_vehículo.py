class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def conducir(self):
        pass
class Auto(Vehiculo):
    def __init__(self, marca, modelo, año, volante):
          super().__init__(marca, modelo, año)
          self.volante = volante

    def conducir(self):
          print(f"Conduciendo el auto {self.marca} {self.modelo} del año {self.año} con volante {self.volante}")

class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, manubrio):
          super().__init__(marca, modelo, año)
          self.manubrio = manubrio


    def conducir(self):
          print(f"Conduciendo la moto {self.marca} {self.modelo} del año {self.año} con manubrio {self.manubrio}")


auto1 = Auto("Toyota", "Corolla", 2020, "de cuero")
moto1 = Moto("Honda", "CBR500R", 2019, "deportivo")
auto1.conducir()
moto1.conducir()