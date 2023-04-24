class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, largeur):
        self.__largeur = largeur

# Création d'un rectangle avec longueur=10 et largeur=5
mon_rectangle = Rectangle(10, 5)

# Modification de la longueur et de la largeur
mon_rectangle.set_longueur(20)
mon_rectangle.set_largeur(10)

# Vérification que les modifications ont été prises en compte
print(mon_rectangle.get_longueur()) # 20
print(mon_rectangle.get_largeur()) # 10