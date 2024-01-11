user_input = input("Introdueix 10 números separats per espais: ")
print(sorted([eval(i) for i in user_input.split()]))