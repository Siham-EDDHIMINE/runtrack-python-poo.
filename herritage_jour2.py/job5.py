# On définit une classe Forme qui prend en paramètres x et y
class Forme:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # On définit une méthode aire qui calcule l'aire de la forme
    def aire(self):
        return self.x * self.y

# On définit une classe Cercle qui hérite de la classe Forme
class Cercle(Forme):
    # On redéfinit la méthode __init__ pour prendre en compte le rayon du cercle
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    # On redéfinit la méthode aire pour calculer l'aire du cercle
    def aire(self):
        return 3.14 * (self.radius ** 2)

# On définit une classe Rectangle qui hérite de la classe Forme
class Rectangle(Forme):
    # On redéfinit la méthode __init__ pour prendre en compte les dimensions du rectangle
    def __init__(self, x, y):
        super().__init__(x, y)

# On crée un objet rectangle à partir de la classe Rectangle
rectangle = Rectangle(10, 20)
# On affiche l'aire du rectangle en appelant la méthode aire de l'objet rectangle
print(rectangle.aire())

# On crée un objet cercle à partir de la classe Cercle
cercle = Cercle(0, 0, 5)
# On affiche l'aire du cercle en appelant la méthode aire de l'objet cercle
print(cercle.aire())