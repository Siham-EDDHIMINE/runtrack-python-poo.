class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def se_presenter(self):
        return f"Je suis {self.prenom} {self.nom}"

personne1 = Personne("Doe", "John")
personne2 = Personne("Dupond", "Jean")

print(personne1.se_presenter())
print(personne2.se_presenter())