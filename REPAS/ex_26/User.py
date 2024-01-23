# Exercici 26

id = 0

class User:
    
    def __init__(self, nom, cognom1, cognom2, edat, sexe):
        global id
        self.user_id = id + 1
        id += 1
        self.nom = nom
        self.cognom1 = cognom1
        self.cognom2 = cognom2
        self.edat = edat
        self.sexe = sexe
    
    # Getters
    def get_user_id(self):
        return self.user_id

    def get_nom(self):
        return self.nom

    def get_cognom1(self):
        return self.cognom1

    def get_cognom2(self):
        return self.cognom2

    def get_edat(self):
        return self.edat

    def get_sexe(self):
        return self.sexe

    # Setters
    def set_nom(self, nom):
        self.nom = nom

    def set_cognom1(self, cognom1):
        self.cognom1 = cognom1

    def set_cognom2(self, cognom2):
        self.cognom2 = cognom2

    def set_edat(self, edat):
        self.edat = edat

    def set_sexe(self, sexe):
        self.sexe = sexe

    # Funcions
    def salutacio(self):
        print(f"ID: {self.user_id}; "
              f"Nom: {self.nom}; "
              f"Primer Cognom: {self.cognom1}; "
              f"Segon Cognom: {self.cognom2}; "
              f"Edat: {self.edat}; "
              f"Sexe: {self.sexe}")
        
    def to_dict(self):
        data = {
            "user_id": self.user_id,
            "nom":self.nom,
            "cognom1": self.cognom1,
            "cognom2": self.cognom2,
            "edat": self.edat,
            "sexe": self.sexe,
        }
        return data

# Instàncies
user1 = User(nom="Roc", cognom1="Bigas", cognom2="Ortuño", edat=22, sexe='M')
user2 = User(nom="Tese Orlando", cognom1="Araujo", cognom2="Sagardoy", edat=20, sexe='M')

user1.salutacio()
print(user1.to_dict())
user2.salutacio()
print(user2.to_dict())
