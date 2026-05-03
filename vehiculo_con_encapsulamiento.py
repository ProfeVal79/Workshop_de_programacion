class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año

    def get_marca(self):
        return self.__marca
    def get_modelo(self):
        return self.__modelo
    def get_año(self):
        return self.__año
    def set_marca(self, marca):
        self.__marca = marca    
    def set_modelo(self, modelo):
        self.__modelo = modelo
    def set_año(self, año):
        self.__año = año

    def conducir(self):
        marca = self.get_marca()
        modelo = self.get_modelo()
        año = self.get_año()
        print(f"Conduciendo el vehículo {marca} {modelo} del año {año}")
        
class Auto(Vehiculo):
    def __init__(self, marca, modelo, año, volante):
          super().__init__(marca, modelo, año)
          self.volante = volante

    def conducir(self):
          print(f"Conduciendo el auto {self.get_marca()} {self.get_modelo()} del año {self.get_año()} con volante {self.volante}")

class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, manubrio):
          super().__init__(marca, modelo, año)
          self.manubrio = manubrio


    def conducir(self):
          print(f"Conduciendo la moto {self.get_marca()} {self.get_modelo()} del año {self.get_año()} con manubrio {self.manubrio}")



auto1 = Auto("Toyota", "Corolla", 2020, "de cuero")
moto1 = Moto("Honda", "CBR500R", 2019, "deportivo")
auto1.conducir()
moto1.conducir()
auto1.set_marca("Ford")
auto1.set_modelo("Focus")
auto1.set_año(2021)
auto1.conducir()