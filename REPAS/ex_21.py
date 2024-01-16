user_input = input("Introdueix els números que vulguis separats per espais (0 = final): ")
data = [int(x) for x in user_input.split()]
print(f"Números de l’usuari: {data}\nSuma total: {sum(data)}\nMitjana: {sum(data) / len(data)}")