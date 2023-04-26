# On définit une classe Rectangle avec des méthodes pour calculer le périmètre et la surface
class Rectangle:
    # La méthode __init__ initialise les attributs de la classe
    def __init__(self, longueur, largeur):
        # Les attributs __longueur et __largeur sont privés car ils commencent par deux underscores
        self.__longueur = longueur
        self.__largeur = largeur

    # La méthode perimetre calcule le périmètre du rectangle
    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    # La méthode surface calcule la surface du rectangle
    def surface(self):
        return self.__longueur * self.__largeur

    # Les méthodes get_longueur et set_longueur permettent d'accéder et de modifier l'attribut __longueur
    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    # Les méthodes get_largeur et set_largeur permettent d'accéder et de modifier l'attribut __largeur
    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, largeur):
        self.__largeur = largeur


# On définit une classe Parallelepipede qui hérite de la classe Rectangle
class Parallelepipede(Rectangle):
    # La méthode __init__ initialise les attributs de la classe
    def __init__(self, longueur, largeur, hauteur):
        # On appelle la méthode __init__ de la classe parente pour initialiser les attributs hérités
        super().__init__(longueur, largeur)
        # L'attribut __hauteur est privé car il commence par deux underscores
        self.__hauteur = hauteur

    # La méthode volume calcule le volume du parallélépipède
    def volume(self):
        # On appelle la méthode surface de la classe parente pour calculer la surface de base du parallélépipède
        return super().surface() * self.__hauteur


# On crée un objet r à partir de la classe Rectangle
r = Rectangle(3, 4)
# On affiche le périmètre et la surface du rectangle en appelant les méthodes perimetre et surface de l'objet r
print(r.perimetre())
print(r.surface())

# On crée un objet p à partir de la classe Parallelepipede
p = Parallelepipede(3, 4, 5)
# On affiche le volume du parallélépipède en appelant la méthode volume de l'objet p
print(p.volume())