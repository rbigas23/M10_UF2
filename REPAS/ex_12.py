mesos = ("gener", "febrer", "març", "abril", "maig", "juny", "juliol", "agost", "setembre", "octubre", "novembre", "desembre")
user_input = None
while not user_input == 0:
    user_input = int(input("Introdueix un número entre 0 i 12: "))
    if user_input > 12:
        print("Número massa gran.")
        continue
    print(mesos[user_input - 1])

