class Student:
    def __init__(self, nom, prenom, num_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__num_etudiant = num_etudiant
        self.__credits = 0
        self.__level = self.__studentEval()

    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            self.__level = self.__studentEval()

    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def studentInfo(self):
        print(f"Nom: {self.__nom}")
        print(f"Prénom: {self.__prenom}")
        print(f"Numéro d'étudiant: {self.__num_etudiant}")
        print(f"Niveau: {self.__level}")

# Création d'un objet Student
john = Student("John", "Doe", 145)

# Ajout de crédits
john.add_credits(20)
john.add_credits(30)
john.add_credits(40)

# Affichage des informations de l'étudiant
john.studentInfo()