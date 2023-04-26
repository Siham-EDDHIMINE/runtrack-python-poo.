# On définit une classe Forme avec une méthode aire qui renvoie 0
class Forme:
    def aire(self):
        return 0

# On définit une classe Rectangle qui hérite de la classe Forme
class Rectangle(Forme):
    # On redéfinit la méthode __init__ pour prendre en compte la largeur et la hauteur du rectangle
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    # On redéfinit la méthode aire pour calculer l'aire du rectangle
    def aire(self):
        return self.largeur * self.hauteur

# On crée un objet rectangle à partir de la classe Rectangle
rectangle = Rectangle(5, 10)
# On affiche l'aire du rectangle en appelant la méthode aire de l'objet rectangle
print(rectangle.aire())