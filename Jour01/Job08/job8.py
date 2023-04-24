class Livre:
    def __init__(self, titre, auteur, annee):
        # Initialisation des attributs de la classe Livre
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.disponible = True

    def verification(self):
        # Vérification de la disponibilité du livre
        return self.disponible

    def emprunter(self):
        # Emprunt du livre si disponible
        if self.verification():
            self.disponible = False
            return True
        else:
            return False

    def rendre(self):
        # Rendre le livre si emprunté
        if not self.verification():
            self.disponible = True
            return True
        else:
            return False

# Création d'un objet Livre
mon_livre = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 1943)

# Emprunt du livre
if mon_livre.emprunter():
    print("Le livre a été emprunté.")
else:
    print("Le livre n'est pas disponible.")

# Rendre le livre
if mon_livre.rendre():
    print("Le livre a été rendu.")
else:
    print("Le livre n'a pas été emprunté.")