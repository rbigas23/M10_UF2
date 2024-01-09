import random
premi = random.randint(1, 100)
found = False
while not found:
    user_input = int(input("Introdueix un número per endevinar el premi: "))
    if not user_input == premi:
        if user_input > premi:
            print("El premi és un número més petit. Torna a provar.")
        else:
            print("El premi és un número més gran. Torna a provar.")
    else:
        found = True
        print(f"El número era {premi}, has guanyat!!")