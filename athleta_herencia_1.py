class Walker:
    def walk(self):
        print("caminando a paso lento...")
class Runner:
    def run(self):
        print("corriendo a toda velocidad...")
class Athlete(Walker, Runner):
    def training(self):
        print("entrenando para la competencia...")
        self.walk()
        self.run()

atleta = Athlete()
atleta.training()