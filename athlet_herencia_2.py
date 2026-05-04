class Walker:
    def training(self):
        print("entrenando caminata...")
class Runner:
    def training(self):
        print("entrenando carrera...")
class Athlete(Walker, Runner):
    def training(self):
        Walker.training(self)
        Runner.training(self) 
        print("entrenamiento completo para la competencia...")

atleta = Athlete()
atleta.training()