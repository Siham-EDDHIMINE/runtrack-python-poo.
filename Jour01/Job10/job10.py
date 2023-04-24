class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, en_marche=False, reservoir=50):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = en_marche
        self.__reservoir = reservoir

    # Mutateurs et accesseurs pour chaque attribut
    def get_marque(self):
        return self.__marque

    def set_marque(self, marque):
        self.__marque = marque

    def get_modele(self):
        return self.__modele

    def set_modele(self, modele):
        self.__modele = modele

    def get_annee(self):
        return self.__annee

    def set_annee(self, annee):
        self.__annee = annee

    def get_kilometrage(self):
        return self.__kilometrage

    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    def get_en_marche(self):
        return self.__en_marche

    def set_en_marche(self, en_marche):
        self.__en_marche = en_marche

    def get_reservoir(self):
        return self.__reservoir

    def set_reservoir(self, reservoir):
        self.__reservoir = reservoir

    # Méthode pour démarrer la voiture
    def demarrer(self):
        if self.verifier_plein() > 5:
            self.set_en_marche(True)
            print("La voiture démarre.")
        else:
            print("Le réservoir est presque vide. La voiture ne peut pas démarrer.")

    # Méthode pour arrêter la voiture
    def arreter(self):
        self.set_en_marche(False)
        print("La voiture s'arrête.")

    # Méthode privée pour vérifier si le réservoir est plein
    def verifier_plein(self):
        return self.get_reservoir()
    
# Création d'un objet voiture
ma_voiture = Voiture("Toyota", "Yaris", 2010, 100000)

# Affichage des informations de la voiture
print("Marque :", ma_voiture.get_marque())
print("Modèle :", ma_voiture.get_modele())
print("Année :", ma_voiture.get_annee())
print("Kilométrage :", ma_voiture.get_kilometrage())
print("En marche :", ma_voiture.get_en_marche())
print("Réservoir :", ma_voiture.get_reservoir())

# Modification des attributs de la voiture
ma_voiture.set_marque("Honda")
ma_voiture.set_modele("Civic")
ma_voiture.set_annee(2015)
ma_voiture.set_kilometrage(50000)

# Affichage des nouvelles informations de la voiture
print("Marque :", ma_voiture.get_marque())
print("Modèle :", ma_voiture.get_modele())
print("Année :", ma_voiture.get_annee())
print("Kilométrage :", ma_voiture.get_kilometrage())

# Démarrage de la voiture
ma_voiture.demarrer()

# Arrêt de la voiture
ma_voiture.arreter()