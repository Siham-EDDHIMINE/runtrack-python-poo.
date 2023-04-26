import random

# On crée une classe Carte avec les attributs valeur et couleur
class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __repr__(self):
        return f"{self.valeur} de {self.couleur}"

# On crée une classe Jeu qui gère l'ensemble des cartes
class Jeu:
    def __init__(self):
        # On crée un paquet de 52 cartes
        self.paquet = []
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
        couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']
        for couleur in couleurs:
            for valeur in valeurs:
                self.paquet.append(Carte(valeur, couleur))
        # On mélange le paquet
        random.shuffle(self.paquet)

    # La méthode tirer_carte permet de tirer une carte du paquet
    def tirer_carte(self):
        return self.paquet.pop()

    # La méthode valeur_main calcule la valeur d'une main en prenant en compte les règles spécifiques du Blackjack
    def valeur_main(self, main):
        valeur = 0
        as_compte = 0
        for carte in main:
            if carte.valeur == 'Valet' or carte.valeur == 'Dame' or carte.valeur == 'Roi':
                valeur += 10
            elif carte.valeur == 'As':
                as_compte += 1
                valeur += 11
            else:
                valeur += int(carte.valeur)
        while as_compte > 0 and valeur > 21:
            valeur -= 10
            as_compte -= 1
        return valeur

# La fonction jouer simule une partie de Blackjack
def jouer():
    jeu = Jeu()
    joueur_main = [jeu.tirer_carte(), jeu.tirer_carte()]
    croupier_main = [jeu.tirer_carte(), jeu.tirer_carte()]

    print(f"Votre main: {joueur_main} (valeur: {jeu.valeur_main(joueur_main)})")
    print(f"Main du croupier: [{croupier_main[0]}, X]")

    while input("Voulez-vous tirer une carte ? (O/N) ").lower() == 'o':
        joueur_main.append(jeu.tirer_carte())
        print(f"Votre main: {joueur_main} (valeur: {jeu.valeur_main(joueur_main)})")
        if jeu.valeur_main(joueur_main) > 21:
            print("Vous avez perdu !")
            return

    while jeu.valeur_main(croupier_main) < 17:
        croupier_main.append(jeu.tirer_carte())

    print(f"Main du croupier: {croupier_main} (valeur: {jeu.valeur_main(croupier_main)})")

    if jeu.valeur_main(croupier_main) > 21 or jeu.valeur_main(joueur_main) > jeu.valeur_main(croupier_main):
        print("Vous avez gagné !")
    else:
        print("Vous avez perdu !")

jouer()