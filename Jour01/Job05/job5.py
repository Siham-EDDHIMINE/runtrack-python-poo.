class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

animal = Animal()
print(f"L'âge de l'animal: {animal.age} ans")
animal.vieillir()
print("# Age de l'animal après appel de la méthode vieillir")
print(f"L'âge de l'animal: {animal.age} ans")

animal = Animal()
animal.prenom = "Luna"
print(f"L'animal se nomme: {animal.prenom}")