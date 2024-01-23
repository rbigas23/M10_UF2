contactes = {'Roger':678232311, 'Oriol':566879326}

def elimina(contactes, user):
    if user in contactes:  # Afegim un if per si no existeix l'usuari
        del contactes[user]
        return contactes[user]
    else:
        return "L'usuari no existeix."  # Si no existeix mostrem aquest missatge per pantalla

print(elimina(contactes, 'Pablo'))
