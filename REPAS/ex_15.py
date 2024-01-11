user_input = input("Introdueix els números que vulguis separats per espais (0 = final): ")
print(sorted([eval(i) for i in user_input.split() if i != '0']))