# On crée une classe Vehicule avec les attributs marque, annee et prix
class Vehicule:
    def __init__(self, marque, annee, prix):
        self.marque = marque
        self.annee = annee
        self.prix = prix

    # La méthode informationsVehicule affiche les attributs en console
    def informationsVehicule(self):
        print(f"Marque: {self.marque}, Année: {self.annee}, Prix: {self.prix}")

# On crée une classe Voiture qui hérite de la classe Vehicule
class Voiture(Vehicule):
    def __init__(self, marque, annee, prix):
        super().__init__(marque, annee, prix)
        # On ajoute l'attribut portes avec une valeur par défaut de 4
        self.portes = 4

    # La méthode informationsVehicule affiche les informations générales du véhicule ainsi que le nombre de portes
    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Portes: {self.portes}")

# On instancie un objet de type Voiture et on appelle la méthode informationsVehicule pour afficher ses informations
voiture = Voiture('Renault', 2020, 15000)
voiture.informationsVehicule()

# On crée une classe Moto qui hérite de la classe Vehicule
class Moto(Vehicule):
    def __init__(self, marque, annee, prix):
        super().__init__(marque, annee, prix)
        # On ajoute l'attribut roue avec une valeur par défaut de 2
        self.roue = 2

    # La méthode informationsVehicule affiche les informations générales du véhicule ainsi que le nombre de roues
    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Roue: {self.roue}")

# On instancie un objet de type Moto et on appelle la méthode informationsVehicule pour afficher ses informations
moto = Moto('Yamaha', 2019, 10000)
moto.informationsVehicule()