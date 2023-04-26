class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print(self.age)

    def bonjour(self):
        print('Hello')

    def modifierAge(self, age):
        self.age = age


class Eleve(Personne):
    def __init__(self):
        super().__init__()

    def allerEnCours(self):
        print('Je vais en cours')

    def affichageAge(self):
        print(f'J’ai {self.age} ans')


class Professeur(Personne):
    def __init__(self, matiereEnseignee, age=40):
        super().__init__(age)
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print('Le cours va commencer')


# Création d'une instance de la classe Eleve
eleve = Eleve()

# Appel de la méthode bonjour de l'élève
eleve.bonjour()

# Appel de la méthode allerEnCours de l'élève
eleve.allerEnCours()

# Modification de l'âge de l'élève à 15 ans
eleve.modifierAge(15)

# Création d'une instance de la classe Professeur avec un âge de 40 ans
professeur = Professeur('Mathématiques')

# Appel de la méthode bonjour du professeur
professeur.bonjour()

# Appel de la méthode enseigner du professeur
professeur.enseigner()