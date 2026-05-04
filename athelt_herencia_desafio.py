class Person:
    def training(self):
        print("Empezando el entenamiento...")

class Walker(Person):
    def training(self):
        super().training()
        print("Caminando a paso lento...")  

class Runner(Person):
    def training(self):
        super().training()
        print("Corriendo a toda velocidad...")

class Athlete(Walker, Runner):
    def training(self):
        super().training()
        print("Entrenamiento completo para la competencia...")

atleta = Athlete()
atleta.training()