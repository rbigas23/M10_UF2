ftotal = int(input('Introdueix el preu de tot el carrito: '))  # Hem de castejar a int



def amb_iva(ftotal, iva = 21):
    ftotal = ftotal + ftotal * iva / 100 #  Falta 'ftotal + ' i ' / 100'  
    return ftotal 


print(amb_iva(ftotal))

# Les funcions es criden després de crear-les
# La variable iva no està definida fora de la funció, a més, ja tenim valor per defecte quan definim la funció (21). No cal posar-la.