# Exercici 25

id = 0

class Vehicle:
    
    def __init__(self, num_rodes, capacitat, preu, autonomia, color):
        global id
        self.vehicle_id = id + 1
        id += 1
        self.num_rodes = num_rodes
        self.capacitat = capacitat
        self.preu = preu
        self.autonomia = autonomia
        self.color = color
        
    # Getters
    def get_vehicle_id(self):
        return self.vehicle_id

    def get_num_rodes(self):
        return self.num_rodes

    def get_capacitat(self):
        return self.capacitat

    def get_preu(self):
        return self.preu

    def get_autonomia(self):
        return self.autonomia

    def get_color(self):
        return self.color

    # Setters
    def set_vehicle_id(self, vehicle_id):
        self.vehicle_id = vehicle_id

    def set_num_rodes(self, num_rodes):
        self.num_rodes = num_rodes

    def set_capacitat(self, capacitat):
        self.capacitat = capacitat

    def set_preu(self, preu):
        self.preu = preu

    def set_autonomia(self, autonomia):
        self.autonomia = autonomia

    def set_color(self, color):
        self.color = color
    
    # Funcions
    def parts(self):
        print(f"ID: {self.vehicle_id}; "
              f"Nombre de Rodes: {self.num_rodes}; "
              f"Capacitat de persones: {self.capacitat}; "
              f"Preu: {self.preu}; "
              f"Autonomia: {self.autonomia}; "
              f"Color: {self.color}")
        
    def to_dict(self):
        data = {
            "vehicle_id": self.vehicle_id,
            "num_rodes": self.num_rodes,
            "capacitat": self.capacitat,
            "preu": self.preu,
            "autonomia": self.autonomia,
            "color": self.color
        }
        return data

#Instàncies
cotxe = Vehicle(num_rodes=4, capacitat=5, preu=25000, autonomia=300, color='vermell')
moto = Vehicle(num_rodes=2, capacitat=4, preu=45000, autonomia=200, color='verd')

cotxe.parts()
print(cotxe.to_dict())
moto.parts()
print(moto.to_dict())
