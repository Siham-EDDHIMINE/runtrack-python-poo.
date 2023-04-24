class Livre:
    def __init__(self, titre, auteur, nombre_de_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_de_pages = nombre_de_pages

    def get_titre(self):
        return self.__titre

    def set_titre(self, titre):
        self.__titre = titre

    def get_auteur(self):
        return self.__auteur

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def get_nombre_de_pages(self):
        return self.__nombre_de_pages

    def set_nombre_de_pages(self, nombre_de_pages):
        if isinstance(nombre_de_pages, int) and nombre_de_pages > 0:
            self.__nombre_de_pages = nombre_de_pages
        else:
            print("Erreur: Le nombre de pages doit être un entier positif.")
 # Création d'un objet Livre
mon_livre = Livre("Simple Justice", "Richard Kluger", 820)

# Affichage des informations du livre
print(f"Titre: {mon_livre.get_titre()}")
print(f"Auteur: {mon_livre.get_auteur()}")
print(f"Nombre de pages: {mon_livre.get_nombre_de_pages()}")

# Modification des informations du livre
mon_livre.set_titre("Simple Justice (édition de luxe)")
mon_livre.set_auteur("Richard Kluger")
mon_livre.set_nombre_de_pages(850)

# Affichage des nouvelles informations du livre
print(f"Titre: {mon_livre.get_titre()}")
print(f"Auteur: {mon_livre.get_auteur()}")
print(f"Nombre de pages: {mon_livre.get_nombre_de_pages()}")   

# Modification des informations du livre
mon_livre.set_titre("Simple Justice (édition de luxe)")
mon_livre.set_auteur("Richard Kluger")
mon_livre.set_nombre_de_pages(850.5)

# Affichage des nouvelles informations du livre
print(f"Titre: {mon_livre.get_titre()}")
print(f"Auteur: {mon_livre.get_auteur()}")
print(f"Nombre de pages: {mon_livre.get_nombre_de_pages()}")